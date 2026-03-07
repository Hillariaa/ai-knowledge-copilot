from app.services.embeddings import embed_texts

texts = [
    "Artificial Intelligence (AI) is revolutionizing industries.",
    "Machine Learning systems rely on high quality data.",
]

vectors = embed_texts(texts)

print("number of embeddings:", len(vectors))
print("Vector length:", len(vectors[0]))
