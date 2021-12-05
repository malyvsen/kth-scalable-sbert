from pathlib import Path


data_path = Path(__file__).parent.parent / "data"
searchable_path = data_path / "news.json"
searchable_vectors_path = data_path / "news_vectors.pkl"
