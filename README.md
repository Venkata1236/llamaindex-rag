# LlamaIndex RAG Demo

A simple Retrieval-Augmented Generation (RAG) project built using LlamaIndex and OpenAI.

This project demonstrates how to:

- Load local documents (PDF and DOCX)
- Convert documents into embeddings
- Build a vector index
- Retrieve relevant document chunks
- Generate answers using a Large Language Model

---

## Architecture Overview

Documents  
→ Chunking  
→ Embeddings  
→ Vector Store Index  
→ Retriever  
→ LLM  
→ Generated Response  

This follows a standard RAG (Retrieval-Augmented Generation) pipeline.

---

## Project Structure

llama_index/

├── main.py  
├── requirements.txt  
├── .gitignore  
├── Documents/  
└── .env   (not pushed to GitHub)  

---

## Installation and Setup

1. Clone the repository

git clone <your_repo_url>  
cd llama_index  

2. Install dependencies

pip install -r requirements.txt  

3. Create a `.env` file in the root directory

OPENAI_API_KEY=your_api_key_here  

4. Run the project

python main.py  

---

## Important Notes

- Do not upload your `.env` file to GitHub.
- Ensure `.env` is included in `.gitignore`.
- OpenAI API usage may incur cost depending on usage.

---

## Adding Documents

Place your PDF or DOCX files inside the "Documents" folder before running the project.

---


## Example Query

Summarize the key points from the documents.

The system retrieves relevant document chunks and generates a contextual response using the LLM.

---

## Technologies Used

- LlamaIndex
- OpenAI API
- Python
- python-dotenv

---

## Learning Objectives

This project was built to understand:

- Retrieval-Augmented Generation (RAG) architecture  
- Embeddings vs LLM workflow  
- Vector indexing  
- Environment variable management  
- Building a simple AI-powered document assistant  

---



- Retrieval-Augmented Generation (RAG): A method that combines document retrieval with language model generation.
- Embedding: A numerical representation of text used for semantic search.
- Vector Store: A database that stores embeddings for similarity search.
- Chunking: Splitting large documents into smaller segments.
- Reproducibility: Ability for others to recreate the project environment easily.