import numpy as np
import pickle
from sbert import run_model, searchable_vectors_path
import streamlit as st


num_best_matches = 5


def main():
    st.title("Semantic search")
    query = st.text_input("Query")
    if query == "":
        return
    query_vector = run_model(query)

    searchable_vectors = load_searchable_vectors()
    searchable_lengths = (
        np.sum(searchable_vectors["vectors"] ** 2, axis=-1) ** 0.5 + 1e-5
    )
    similarities = (
        np.sum(searchable_vectors["vectors"] * query_vector, axis=-1)
        / searchable_lengths
        / np.sum(query_vector ** 2) ** 0.5
    )
    most_similar = np.argsort(similarities)[-num_best_matches:][::-1]

    for similar_index in most_similar:
        with st.expander(searchable_vectors["headlines"][similar_index]):
            st.write(f"{similarities[similar_index] * 100:.0f}% match")


@st.cache()
def load_searchable_vectors():
    with open(searchable_vectors_path, "rb") as searchable_vectors_file:
        return pickle.load(searchable_vectors_file)


main()
