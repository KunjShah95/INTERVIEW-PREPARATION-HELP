from fastapi import FastAPI, HTTPException
from langchain_agent import generate_answer_with_langchain

app = FastAPI()

@app.get("/")
async def read_root():
    """Serve the HTML frontend."""
    with open("templates/index.html") as f:
        return f.read()

@app.post("/summarize")
async def summarize_answer(question: str, model: str = "claude"):
    """Generate an answer using Claude AI or Gemini AI, or query the VectorDB."""
    try:
        # Option 1: Use Langchain (Claude AI or Gemini AI)
        answer = generate_answer_with_langchain(question, model)

        # Option 2: Query VectorDB for relevant knowledge
        # answer = query_knowledge(question)

        # Optionally store new Q&A into VectorDB
        # embed_and_store_knowledge(question, answer)

        return {"answer": answer}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=3000)
