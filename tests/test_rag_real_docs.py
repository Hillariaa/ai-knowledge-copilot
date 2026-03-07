from app.services.rag_pipeline import answer_question

question = "What problem does Retrieval Augmented Generation Solve?"

result = answer_question(question)

print("Question:", question)
print()

print("Answer:")
print(result["answer"])
print()

print("Sources:")
for s in result["sources"]:
    print("-", s)
