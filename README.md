# PDF Analyzer

## Description

The PDF Analyzer is a project that aims to analyze and extract information from PDF documents. It provides a streamlined process for extracting text, images, and metadata from PDF files. With the help of OpenAI and Huggingface models, the application leverages advanced natural language processing techniques to perform tasks such as text summarization, sentiment analysis, and entity recognition. The PDF Analyzer is built using Python and utilizes popular libraries like Streamlit and PyPDF2. It offers a user-friendly interface for uploading PDF files, selecting analysis options, and viewing the results. Whether you need to quickly extract key information from a PDF document or gain insights from large volumes of PDF files, the PDF Analyzer is a powerful tool that simplifies the process and enhances productivity.

## Installation

To install the dependencies for this project, run the following command:

```
pip install -r requirements.txt
```

## Running Steps

Before running the application you must create a .env file with your OpenAI and Huggingfce tokens like this:

```
OPENAI_API_KEY="{YOUR_TOKEN}"
HUGGINGFACEHUB_API_TOKEN="{YOUR_TOKEN}"
```

In order to run the application run the following command:

```
streamlit run app.py
```
