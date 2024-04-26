import re
import numpy as np
import pandas as pd
from glob import glob
from ast import literal_eval
from openai import OpenAI
from numpy.typing import NDArray
from .color_logger import get_logger
from .settings import Settings
from .cost import Cost
from ._types import Embedding


class Embedder:
    def __init__(self) -> None:
        self.embedding_model = Settings().embeddings.model
        self.client = OpenAI()
        self.cost = Cost()

    def generate_embeddings(self, texts: list[str]) -> list[Embedding]:
        texts = [text.replace('\n', ' ') for text in texts]
        response = self.client.embeddings.create(input=texts, model=self.embedding_model)
        self.cost.add('embedding_tokens', amount=response.usage.total_tokens)
        embeddings = [emb.embedding for emb in response.data]
        return embeddings


class Archive:
    def __init__(self) -> None:
        self.embedder = Embedder()
        self.logger = get_logger()
        self.db: pd.DataFrame = self._get_data_from_dir()

    def _get_data_from_dir(self) -> pd.DataFrame:
        embeddings_dir: str = Settings().archive
        if not embeddings_dir.endswith('/'): embeddings_dir += '/'
        self.logger.info(f"Loading archive from: {embeddings_dir}")
        dfs: list[pd.DataFrame] = list()
        for filename in glob(embeddings_dir + '*.csv'):
            dfs.append(pd.read_csv(filename, index_col=None, header=0))
        if len(dfs) > 0:
            self.logger.debug(f"Found {len(dfs)} files in archive")
            df = pd.concat(dfs, axis=0, ignore_index=True)
            df['embedding'] = df['embedding'].apply(literal_eval)
            df['searchable_title'] = df['title'].apply(self._get_searchable_title)
            return df
        else:
            self.logger.warn("Found no files in archive directory!", color='red')
            return pd.DataFrame()
        
    @property
    def empty(self) -> bool:
        return self.db.empty
    
    @staticmethod
    def _get_searchable_title(title: str) -> str:
        title = title.strip().replace('-', ' ')
        title = re.sub(r'\s', ' ', title)
        title = re.sub(r' +', ' ', title)
        title = re.sub(r'[^A-Za-z0-9 ]+', '', title)
        title = title.lower()
        return title

    @staticmethod
    def cosine_similarity(vector: Embedding, matrix: list[Embedding]) -> NDArray:
        # Normalize the vector
        vector_array = np.expand_dims(vector, axis=1)
        vector_norm = np.linalg.norm(vector_array)
        vector_normalized = vector_array / vector_norm  # type: ignore

        # Normalize each row in the matrix
        matrix_norm = np.linalg.norm(matrix, axis=1)  # type: ignore
        matrix_normalized = matrix / matrix_norm[:, np.newaxis]

        # Compute cosine similarity
        similarity = np.dot(matrix_normalized, vector_normalized)
        return similarity

    def top_indices_by_cosine_similarity(self, vector: Embedding, matrix: list[Embedding], k: int) -> list[int]:
        sim = self.cosine_similarity(vector, matrix)  
        sim = np.squeeze(sim)
        if len(sim.shape) == 0: 
            sim = np.expand_dims(sim, axis=0)
        
        top_indices = np.argpartition(sim, -k)[-k:].tolist()
        return top_indices

    def query(self, query: str, max_results: int) -> pd.DataFrame:
        if self.empty:
            return pd.DataFrame()
        query_embedding = self.embedder.generate_embeddings([query])[0]
        embeddings = list(self.db['embedding'].to_list())
        top_indices = self.top_indices_by_cosine_similarity(query_embedding, embeddings, k=max_results)
        return self.db.iloc[top_indices]

    def get_by_title(self, title: str) -> pd.Series:
        if self.empty:
            return pd.Series()
        df = self.db[self.db['searchable_title'] == self._get_searchable_title(title)]
        if df.empty:
            self.logger.warn(f"Tried to get title \"{title}\" from archive, but it does not exist")
            return pd.Series()
        else:
            return df.iloc[0]
