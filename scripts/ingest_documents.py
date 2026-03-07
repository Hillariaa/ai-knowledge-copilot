from pathlib import Path

from pypdf import PdfReader
from docx import Document

from data.chunking import create_chunks
from app.services.retrieval import store_chunks

DOCUMENT_FOLDER = "documents"


def load_pdf(path: Path) -> str:
    reader = PdfReader(str(path))
    text = ""

    for page in reader.pages:
        text += page.extract_text() + "\n"

    return text


def load_docx(path: Path) -> str:
    doc = Document(str(path))
    text = "\n".join(p.text for p in doc.paragraphs)
    return text


def load_document(path: Path) -> str:

    if path.suffix == ".pdf":
        return load_pdf(path)

    if path.suffix == ".docx":
        return load_docx(path)

    return ""


def ingest():
    folder = Path(DOCUMENT_FOLDER)

    for file in folder.iterdir():
        print(f"Ingesting: {file.name}")

        text = load_document(file)

        chunks = create_chunks(text)

        store_chunks(chunks, source=file.name)


if __name__ == "__main__":
    ingest()
