from fastapi import FastAPI

from app.api.routes import router

app = FastAPI(
    title="AI Knowledge Copilot API",
    description="Enterprise-style RAG system",
    version="1.0",
)

app.include_router(router)
