from sbert import run_model
import streamlit as st


def main():
    st.title("Semantic search")
    query = st.text_input("Query")
    if query == "":
        return
    sentence_vector = run_model(query)
    st.write(sentence_vector.shape)


main()
