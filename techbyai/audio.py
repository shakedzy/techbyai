import io
from datetime import datetime
from openai import OpenAI
from pydub import AudioSegment
from concurrent.futures import ThreadPoolExecutor
from .utils import ordinal_number, path_to_resource, domain_of_url
from .settings import Settings
from .cost import Cost
from .item_suggestion import ItemSuggestion


class Narrator:
    def __init__(self) -> None:
        self.client = OpenAI()
        self.cost = Cost()

    def narrate(self, items: list[ItemSuggestion], title: str) -> AudioSegment:
        ranked_items = [item for item in items if item.rank > 0]
        ranked_items = sorted(ranked_items, key=lambda s: s.rank)
        with ThreadPoolExecutor() as executor:
            futures = [executor.submit(self._narrate_single_article, item, idx) for idx, item in enumerate(ranked_items, start=1)]
            title_future = executor.submit(self._narrate_title, title)
        segments = [f.result() for f in futures]
        title_segment = title_future.result()
        self.cost.add('tts_chars', amount=sum([len(item.text) for item in ranked_items]))
        output_audio = AudioSegment.empty()
        output_audio += title_segment
        for segment in segments:
            output_audio += segment
        output_audio += (AudioSegment.silent(duration=1000) + AudioSegment.from_mp3(path_to_resource('outro.mp3')) + AudioSegment.silent(duration=1000))
        return output_audio

    def _narrate_single_article(self, item: ItemSuggestion, idx: int) -> AudioSegment:
        response = self.client.audio.speech.create(
            model=Settings().tts.model,
            voice=Settings().tts.voice,
            input=f"Article {idx} - {item.title}\nFrom: {domain_of_url(item.url)}\n\n{item.text}"
        )
        audio_data = io.BytesIO(response.content) 
        audio_segment = AudioSegment.silent(duration=1000) + AudioSegment.from_file(audio_data, format="mp3")
        return audio_segment
    
    def _narrate_title(self, title: str) -> AudioSegment:
        now = datetime.now()
        date_str = f"{now.strftime('%B')} {ordinal_number(now.day)}, {now.year}"
        speech_input = f"{Settings().editorial.name}: {date_str} - {title}"
        self.cost.add('tts_chars', amount=len(speech_input))
        response = self.client.audio.speech.create(
            model=Settings().tts.model,
            voice=Settings().tts.voice,
            input=speech_input
        )
        audio_data = io.BytesIO(response.content) 
        audio_segment = AudioSegment.silent(duration=1000) + AudioSegment.from_file(audio_data, format="mp3")
        return audio_segment
    