from data.chunking import create_chunks

sample_text = """
Artificial Intelligence (AI) is revolutionizing industries.
Machine Learning systems rely on high quality data.
Retrieval Augmented Generation (RAG) improves factual accuracy.
"""

chunks = create_chunks(sample_text)

print("chunks:")
for c in chunks:
    print("---")
    print(c)
