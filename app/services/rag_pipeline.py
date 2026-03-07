from openai import OpenAI
import os
from dotenv import load_dotenv
from app.services.retrieval import retrieve

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def rerank_chunks(question, chunks):

    prompt = f"""
    You are ranking document chunks by relevance.
    
    Question:
    {question}
    
    Chunks:
    """

    for i, c in enumerate(chunks):
        prompt += f"\nChunk {i}:\n{c['text']}\n"

    prompt += """
    Return the 5 most relevant chunk numbers as a comma separated list.
    Example: 3,1,7,0,2
    """

    response = client.chat.completions.create(
        model="gpt-4.1-mini", messages=[{"role": "user", "content": prompt}]
    )

    ranking = (response.choices[0].message.content or "").strip()

    indexes = [int(i) for i in ranking.split(",")]

    return [chunks[i] for i in indexes if i < len(chunks)]


def answer_question(question: str):

    # Retrieve relevant chunks
    retrieved_chunks = retrieve(question)

    context_chunks = rerank_chunks(question, retrieved_chunks)

    context = "\n\n".join([c["text"] for c in context_chunks])

    print("Retrieved context:")
    for c in context_chunks:
        print("---")
        print("SOURCE:", c["source"])
        print(c["text"])

    # Build prompt
    prompt = f"""
    You are a helpful assistant.
    Use ONLY the context below to answer the question.
    If the answer is not in the context, say "I don't know".

    Context:
    {context}

    Question:
    {question}

    Answer:
    """

    # Call LLM
    response = client.chat.completions.create(
        model="gpt-4.1-mini", messages=[{"role": "user", "content": prompt}]
    )

    answer = response.choices[0].message.content

    sources = list({c["source"] for c in context_chunks})

    return {"answer": answer, "sources": sources}
