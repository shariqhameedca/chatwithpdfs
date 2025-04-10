import streamlit as st
import google.generativeai as genai
import os

from dotenv import load_dotenv
from src import user_input, get_pdf_text, get_text_chunks, get_vector_store

load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))


def main():
    st.set_page_config("Multi PDF Chatbot", page_icon=":scroll:")
    st.header("Multi-PDF's 📚 - Chat Agent 🤖 ")

    user_question = st.text_input("Ask a Question from the pdf Files uploaded...")

    if user_question:
        user_input(user_question=user_question, st=st)

    with st.sidebar:
        st.title("📁 PDF File's Section")
        pdf_docs = st.file_uploader(
            "Upload your PDF Files \n & Click on the Submit & Process Button",
            accept_multiple_files=True,
        )

        if st.button("Submit & Process"):
            with st.spinner("Processing..."):
                raw_text = get_pdf_text(pdf_docs)
                text_chunks = get_text_chunks(raw_text)

                get_vector_store(text_chunks)
                st.success("Done")

        st.write("---")


if __name__ == "__main__":
    main()
