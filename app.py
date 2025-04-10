import streamlit as st
import google.generativeai as genai
import os

from dotenv import load_dotenv
from src import user_input, get_pdf_text, get_text_chunks, get_vector_store

load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))


def main():
    st.set_page_config("Multi PDF Chatbot", page_icon=":scroll:")
    st.header("Multi PDFs Chatbot - 🤖 ")

    user_question = st.text_input("Ask a Question from your uploaded PDF")

    if user_question:
        user_input(user_question=user_question, st=st)

    with st.sidebar:
        st.title("📁 PDF Files")
        pdf_docs = st.file_uploader(
            "Upload your PDF Files \n & Click Submit",
            accept_multiple_files=True,
        )

        if st.button("Submit"):
            with st.spinner("Parsing..."):
                raw_text = get_pdf_text(pdf_docs)
                text_chunks = get_text_chunks(raw_text)

                get_vector_store(text_chunks)
                st.success("Parsing Complete")

        st.write("---")


if __name__ == "__main__":
    main()
