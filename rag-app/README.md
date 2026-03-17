# AI Powerlifting Analytics Assistant using Endee (RAG)

## Problem Statement
Powerlifting athletes, coaches, and analysts often struggle to explore large competition datasets efficiently. Manually filtering thousands of athlete records is time-consuming and difficult. This project provides a Retrieval-Augmented Generation (RAG)-style analytics assistant that enables natural-language querying over powerlifting performance data.

## Project Overview
This project uses a real-world Kaggle powerlifting dataset to build an AI-powered semantic search assistant. The system converts athlete performance records into text, generates embeddings, and retrieves the most relevant records for a user query.

## Practical Use Case
- Find athletes with similar performance profiles
- Retrieve top relevant lifters for natural-language questions
- Explore deadlift, squat, bench press, and total lift performance using semantic search

## System Architecture (RAG Pipeline)

1. Data Ingestion  
   - Load Kaggle powerlifting dataset  

2. Data Processing  
   - Clean and filter relevant columns  
   - Convert structured rows into natural-language text  

3. Embedding Generation  
   - Use Sentence Transformers (`all-MiniLM-L6-v2`)  

4. Vector Search (Endee-aligned design)  
   - Store embeddings  
   - Perform similarity search using cosine similarity  

5. Retrieval-Augmented Response  
   - Retrieve top relevant records  
   - Generate final answer (offline RAG simulation)

## Technologies Used

- Python  
- Pandas  
- Sentence Transformers  
- Scikit-learn (cosine similarity)  
- Jupyter Notebook  
- Endee (vector database concept & integration design)

## Why Endee

Endee is a high-performance vector database designed for large-scale similarity search.  
This project follows Endee’s architecture by:
- converting data into embeddings  
- performing vector similarity search  
- enabling semantic retrieval  

Due to local environment constraints, cosine similarity is used to simulate vector search behavior consistent with Endee’s design.





## Setup Instructions

### 1. Clone the repository
```bash
git clone https://github.com/your-username/endee.git
cd endee/rag-app

### 2. Create virtual environment
```bash
python3 -m venv venv
source venv/bin/activate


### 3. Install dependencies
```bash
pip install pandas sentence-transformers scikit-learn jupyter

### 4. Run the notebook
```bash
jupyter notebook
