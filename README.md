# Multi-PDF Chatbot - 🤖

## Description

This Streamlit application allows users to upload multiple PDF files and ask questions based on the content of those documents. It utilizes Google's Generative AI models to provide answers by first processing the PDFs, extracting text, chunking it, and creating a vector store for efficient semantic search.

## Features

- **Upload Multiple PDFs:** Users can upload and process several PDF files at once.
- **Ask Questions:** Interact with the combined content of the uploaded PDFs by asking natural language questions.
- **AI-Powered Answers:** Leverages Google's Generative AI to understand the context of your questions and provide relevant answers based on the PDF content.
- **Streamlit Interface:** Provides a user-friendly web interface for easy interaction.
- **Progress Indication:** Shows a "Processing..." spinner during the PDF processing stage.
- **Success Confirmation:** Displays a "Done" message upon successful processing of the PDF files.

## Installation Guide

1.  **Clone the repository:**
    ```bash
    git clone <repository_url>
    cd <repository_directory>
    ```

2.  **Create a virtual environment (recommended):**
    ```bash
    conda create -n chatbot python=3.11 -y
    conda activate chatbot
    ```

3.  **Install the required dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
    *(Ensure that the `requirements.txt` file in the repository contains the necessary libraries, such as `streamlit`, `google-generativeai`, `python-dotenv`, `pypdf`, `langchain`, and `tiktoken`.)*

4.  **Set up your Google Cloud API Key:**
    - Go to the [Google Cloud Console](https://console.cloud.google.com/).
    - Create a new project or select an existing one.
    - Enable the Generative Language API.
    - Create API credentials (if you haven't already).
    - Download the API key as a JSON file.

5.  **Create a `.env` file:**
    - In the root directory of your project, create a file named `.env`.
    - Add your Google API key to this file:
      ```
      GOOGLE_API_KEY="YOUR_GOOGLE_API_KEY"
      ```
      *(Replace `"YOUR_GOOGLE_API_KEY"` with the actual API key from the downloaded JSON file.)*

## Running Guide

1.  **Navigate to the project's root directory in your terminal.**

2.  **Ensure your virtual environment is activated:**
    ```bash
    source venv/bin/activate  # On macOS and Linux
    venv\Scripts\activate  # On Windows
    ```

3.  **Run the Streamlit application:**
    ```bash
    streamlit run app.py
    ```

4.  **The application will open in your web browser.** You can then upload your PDF files using the file uploader in the sidebar and ask questions in the main section. Click the "Submit" button to process the PDFs before asking questions.
