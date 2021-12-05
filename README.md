# S-BERT for semantic search

An assignment for the Scalable Machine Learning course at KTH.

This project uses [Poetry](https://python-poetry.org/). If you don't know it, check out the short guide I wrote [here](https://github.com/malyvsen/instructions/blob/main/poetry.md) :)

## File organization

- The data or symbolic links to it live under `data/`
- `index.py` indexes the file under `data/news.json`, producing `data/news_vectors.pkl`
- `semantic_search.py` is the actual app, to run it, do `streamlit run semantic_search.py`
- `sbert/` contains the backstage code
