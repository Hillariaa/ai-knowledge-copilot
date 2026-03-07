from typing import List
import re


def split_text_into_sentences(text: str) -> List[str]:
    """
    Simple sentence splitter.
    """
    sentences = re.split(r"(?<=[.!?]) +", text)
    return sentences


def create_chunks(text: str, chunk_size: int = 3, overlap: int = 1) -> List[str]:
    """
    Create overlapping text chunks from sentences.
    """
    sentences = split_text_into_sentences(text)

    chunks = []

    for i in range(0, len(sentences), chunk_size - overlap):
        chunk = " ".join(sentences[i : i + chunk_size])
        chunks.append(chunk)

    return chunks
