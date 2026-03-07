from chromadb.api.types import Metadata
import chromadb
from typing import List
from app.services.embeddings import embed_texts

# Create a persistent client
client = chromadb.PersistentClient(path="vector_db")

# Create a collection
collection = client.get_or_create_collection(name="documents")
print("Documents currently in DB:", collection.count())


def store_chunks(chunks: List[str], source: str):
    """
    Store documents and their embeddings.
    """

    embeddings = embed_texts(chunks)

    ids = [f"chunk_{i}" for i in range(len(chunks))]

    metadatas: List[Metadata] = [{"source": source} for _ in chunks]

    collection.add(
        documents=chunks,
        embeddings=[list(e) for e in embeddings],
        ids=ids,
        metadatas=metadatas,
    )


def retrieve(query: str, k: int = 20):

    query_embedding = embed_texts([query])[0]

    results = collection.query(query_embeddings=[query_embedding], n_results=k)

    if results is None:
        return []

    documents = results["documents"][0]  # pyright: ignore[reportOptionalSubscript]
    metadatas = results["metadatas"][0]  # pyright: ignore[reportOptionalSubscript]

    retrieved = []

    for doc, meta in zip(documents, metadatas):
        source = "unknown"

        if meta is not None and "source" in meta:
            source = meta["source"]

        retrieved.append({"text": doc, "source": source})

    return retrieved
