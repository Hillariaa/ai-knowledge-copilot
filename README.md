# AI Knowledge Copilot

A **Retrieval-Augmented Generation (RAG) AI assistant** that answers questions using your own documents.

The system ingests PDFs and DOCX files, converts them into embeddings, stores them in a vector database, retrieves relevant context, and generates grounded answers using an LLM.

This project demonstrates how modern AI copilots are built using **RAG architecture, vector databases, and LLM APIs**.

---

# Features

- Document ingestion pipeline (PDF + DOCX)
- Text chunking for semantic retrieval
- OpenAI embeddings for vector search
- ChromaDB vector database
- Semantic document retrieval
- RAG prompt construction
- LLM-generated answers with sources
- FastAPI REST API
- Docker containerization

---

# Architecture

The system follows a **Retrieval Augmented Generation (RAG)** architecture.

```
User Question
      ↓
FastAPI Endpoint
      ↓
RAG Pipeline
      ↓
Vector Retrieval (ChromaDB)
      ↓
Relevant Document Chunks
      ↓
Prompt Construction
      ↓
OpenAI LLM
      ↓
Answer + Sources
```

### Query Pipeline

```
User Question
      ↓
FastAPI Endpoint
      ↓
RAG Pipeline
      ↓
Vector Retrieval (ChromaDB)
      ↓
Relevant Document Chunks
      ↓
Prompt Construction
      ↓
OpenAI LLM
      ↓
Answer + Sources
```

Document Ingestion Pipeline

```
Documents (PDF / DOCX)
      ↓
Loaders
      ↓
Chunking
      ↓
Embeddings
      ↓
Vector Database (ChromaDB)
```

---

# Project Structure

```
ai-knowledge-copilot
│
├── app
│   ├── main.py
│   ├── api
│   │   └── routes.py
│   └── services
│       ├── embeddings.py
│       ├── retrieval.py
│       ├── rag_pipeline.py
│       └── reranker.py
│
├── data
│   └── chunking.py
│
├── scripts
│   └── ingest_documents.py
│
├── documents
│   └── (PDF / DOCX files)
│
├── vector_db
│
├── Dockerfile
├── requirements.txt
├── pyproject.toml
└── README.md
```

---

# Installation

Clone the repository:

```
git clone https://github.com/yourusername/ai-knowledge-copilot.git
cd ai-knowledge-copilot
```

Create environment:

```
uv venv
```

Activate environment:

Mac / Linux

```
source .venv/bin/activate
```

Windows

```
.venv\Scripts\activate
```

Install dependencies:

```
uv pip install -r requirements.txt
```

---

# Add Documents

Place files inside the `documents/` folder.

Supported formats:

- PDF
- DOCX

---

# Ingest Documents

Run the ingestion pipeline:

```
uv run python -m scripts.ingest_documents
```

This will:

- Load documents
- Split into chunks
- Generate embeddings
- Store them in ChromaDB

---

# Run the API

Start the FastAPI server:

```
uv run uvicorn app.main:app --reload
```

Open the API docs:

```
http://localhost:8000/docs
```

---

# Example API Request

Endpoint:

```
POST /ask
```

Example request:

```
{
  "question": "What problem does Retrieval Augmented Generation solve?"
}
```

Example response:

```
{
  "answer": "...generated answer...",
  "sources": ["rag-paper.pdf"]
}
```

---

# Running with Docker

Build container:

```
docker build -t ai-knowledge-copilot .
```

Run container:

```
docker run -p 8000:8000 ai-knowledge-copilot
```

Access API:

```
http://localhost:8000/docs
```

---

# Technologies Used

- Python
- FastAPI
- OpenAI API
- ChromaDB
- Vector embeddings
- Retrieval Augmented Generation (RAG)
- Docker

---

# Future Improvements

Potential extensions:

- Streaming responses
- Authentication
- Web chat interface
- Hybrid search (BM25 + vector)
- Production vector DB (Pinecone / Weaviate / Qdrant)
- Document metadata filtering
- Redis caching
- Background ingestion workers

---

# Learning Goals

This project was built to explore the architecture behind modern AI assistants and knowledge copilots.

It demonstrates:

- RAG system design
- Vector search
- Document pipelines
- API design
- Containerized AI services

---

# License

MIT License

