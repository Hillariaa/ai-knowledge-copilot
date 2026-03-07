from app.services.rag_pipeline import answer_question
from data.chunking import create_chunks
from app.services.retrieval import store_chunks

text = """
Artificial Intelligence is transforming industries.
Machine Learning relies on large datasets.
Retrieval Augmented Generation improves factual accuracy.
Embeddings allow semantic search across documents.
"""

chunks = create_chunks(text)

store_chunks(chunks)

answer = answer_question("What improves factual accuracy?")

print("Answer:")
print(answer)
