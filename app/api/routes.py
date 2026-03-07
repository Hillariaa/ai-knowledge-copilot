from fastapi import APIRouter
from pydantic import BaseModel
from app.services.rag_pipeline import answer_question

router = APIRouter()


class QuestionRequest(BaseModel):
    question: str


@router.post("/ask")
def ask_question(request: QuestionRequest):
    """
    Ask a question to the RAG system.
    """

    result = answer_question(request.question)

    return result
