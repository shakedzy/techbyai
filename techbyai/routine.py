import json
from textwrap import dedent
from concurrent.futures import ThreadPoolExecutor
from .assistant import Assistant
from .color_logger import get_logger


class Routine:
    NUM_OF_REPORTERS = 4
    TOPICS = dedent(
        """
        Foundation Models, AI Ethics and Bias, AI in Healthcare, Generative AI, AI in Creative Industries,
        AI Regulation and Policy, AI and Cybersecurity, AI in Education, AI and Climate Change, AI in Robotics,
        AI in Gaming, Promising startups in Generative AI, Distinguished companies (like OpenAI, Anthropic, Mistral, 
        Google, Cohere, Microsoft, Amazon, Midjourney, Stability, etc.)
        """.strip())

    def __init__(self) -> None:
        self.editor = self._get_editor() 
        self.reporters: list[Assistant] = []
        self.names: list[str] = []
        self.logger = get_logger()

    def _get_editor(self) -> Assistant:
        return Assistant(definition="You are the Editor-in-Chief of a daily tech magazine")
    
    def _hire_reporters(self) -> tuple[list[Assistant], list[str]]:
        task = dedent(
            f"""
            You must hire {self.NUM_OF_REPORTERS} reporters to research, choose and write the articles
            for today's issue about the latest news and trends in tech and AI. 
            Describe each of the 4 individuals you hire for this task.
            Your response should be a JSON, where the keys are the names of the reporters (which you generate),
            and the values are their characteristics description.
            IMPORTANT: Describe their characteristics as if you are talking to each one of them, in second body.
            """.strip())
        response = self.editor.do(task, as_json=True)
        reporters = []
        names = []
        for name, description in json.loads(response).items()[:self.NUM_OF_REPORTERS]:
            names.append(name)
            reporters.append(Assistant(description))
        return reporters, names
    
    def _research(self, items_per_reporter: int = 5) -> list[dict[str, str]]:
        editor_task = dedent(
            f"""
            Brief your staff about the type of news you'd like them to look for for today's issue.
            Explain to them what you're expecting of them. Here are some example topics:
            {self.TOPICS}
            Feel free to edit, add or remove topics as you wish.
            Reply as if you speak to your reporters directly.
            """)
        editor_response = self.editor.do(editor_task)
        reporters_task = dedent(
            f"""
            {editor_response}
            IMPORTANT GUIDELINES:
            - Search the web and read webpages to complete your assignment. Make as many searches as required
            - You must provide AT LEAST {items_per_reporter} items
            - Your response should be formatted as JSON, where the items titles are the keys, and the 
              values are the items URLs
            """.strip())
        
        with ThreadPoolExecutor() as executor:
            futures = [executor.submit(reporter.do, reporters_task, as_json=True) for reporter in self.reporters]
        results = [json.loads(f.result()) for f in futures]
        return results

    def do(self) -> None:
        self.logger.info("Hiring staff")
        self.reporters, self.names = self._hire_reporters()
        self.logger.info("Performing research")
        suggestions = self._research()