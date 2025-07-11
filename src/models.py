from pydantic import BaseModel
from typing import Optional

class TextRequest(BaseModel):
    text: str

class TextResponse(BaseModel):
    success: bool
    processed_text: Optional[str] = None
    error: Optional[str] = None
