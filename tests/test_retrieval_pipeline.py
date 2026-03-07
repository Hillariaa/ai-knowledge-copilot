from data.chunking import create_chunks
from app.services.retrieval import store_chunks, retrieve

text = """
Artificial Intelligence is transforming industries.
Machine Learning relies on large datasets.
Retrieval Augmented Generation(RAG) improves factual accuracy.
Embeddings allow semantic search across documents.
"""

chunks = create_chunks(text)

store_chunks(chunks, source)  # noqa: F821  # pyright: ignore[reportUndefinedVariable]

results = retrieve("What improves factual accuracy?")

print("Retrieved chunks:")
for r in results:
    print("---")
    print(r)
