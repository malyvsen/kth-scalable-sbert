# S-BERT for semantic search

An assignment for the Scalable Machine Learning course at KTH.

This project uses [Poetry](https://python-poetry.org/). If you don't know it, check out the short guide I wrote [here](https://github.com/malyvsen/instructions/blob/main/poetry.md) :)

## Try it out!

1. Download the trained models from [here](https://drive.google.com/file/d/1MYX2Ud4rRGskr2poUeAkf1nYCFe_wwo3/view). Place them under `checkpoints/`.
1. Downlaod the data from [here](https://www.kaggle.com/rmisra/news-category-dataset) and put it under `data/`.
1. Install [Poetry](https://python-poetry.org/) if you haven't already.
1. Run `poetry install` to create a virtual environment.
1. Run `poetry run python index.py` to index the news headlines.
1. Run `poetry run streamlit run semantic_search.py` and a browser should launch with the interface!

## File organization

- The data or symbolic links to it live under `data/`
- `index.py` indexes the file under `data/news.json`, producing `data/news_vectors.pkl`
- `semantic_search.py` is the actual app, to run it, do `streamlit run semantic_search.py`
- `sbert/` contains the backstage code
