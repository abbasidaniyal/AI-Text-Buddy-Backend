from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from src.models import TextRequest, TextResponse
from src.service import process_text_with_ai, FIX_PROMPT, REWRITE_PROMPT

app = FastAPI(title="AI Text Assistant Backend", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/health")
async def health_check():
    return {
        "status": "healthy",
        "message": "Backend is running"
    }

@app.post("/fix-text", response_model=TextResponse)
async def fix_text(request: TextRequest):
    if not request.text.strip():
        return TextResponse(success=False, error="Empty text provided")
    processed_text = await process_text_with_ai(request.text, FIX_PROMPT)
    return TextResponse(success=True, processed_text=processed_text)

@app.post("/rewrite-text", response_model=TextResponse)
async def rewrite_text(request: TextRequest):
    if not request.text.strip():
        return TextResponse(success=False, error="Empty text provided")
    processed_text = await process_text_with_ai(request.text, REWRITE_PROMPT)
    return TextResponse(success=True, processed_text=processed_text)

@app.get("/")
async def root():
    return {"message": "AI Text Assistant Backend"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
