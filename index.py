import json
import numpy as np
import pickle
from sbert import run_model, searchable_path, searchable_vectors_path
from tqdm.auto import tqdm


with open(searchable_path) as searchable_file:
    headlines = [
        json.loads(article_data)["headline"]
        for article_data in searchable_file.read().split("\n")
        if article_data != ""
    ]

vectors = np.stack(
    [
        run_model(headline)
        for headline in tqdm(headlines, desc="Indexing news headlines")
    ]
)
with open(searchable_vectors_path, "wb") as vectorized_file:
    pickle.dump({"headlines": headlines, "vectors": vectors}, vectorized_file)
