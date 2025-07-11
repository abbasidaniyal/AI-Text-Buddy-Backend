from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage
from fastapi import HTTPException
import logging

from dotenv import load_dotenv, find_dotenv
# Load environment variables
load_dotenv(find_dotenv())

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize OpenAI
try:
    llm = ChatOpenAI(
        model="gpt-3.5-turbo",
        temperature=0.3,
        max_tokens=1000
    )
    logger.info("OpenAI client initialized successfully")
except Exception as e:
    logger.error(f"Failed to initialize OpenAI client: {e}")
    llm = None

# System prompts
FIX_PROMPT = """You are a text correction assistant. Your task is to fix grammar, spelling, punctuation, and basic readability issues in the given text while preserving the original meaning and style as much as possible.

Rules:
- Fix grammatical errors
- Correct spelling mistakes
- Improve punctuation
- Maintain the original tone and style
- Keep the same length approximately
- Do not change the core message or meaning
- Return only the corrected text, no explanations

Text to fix:"""

REWRITE_PROMPT = """You are a text rewriting assistant. Your task is to rewrite the given text to make it clearer, more engaging, and better structured while maintaining the core message.

Rules:
- Improve clarity and readability
- Enhance flow and structure
- Make it more engaging if appropriate
- Fix any grammar or spelling issues
- You can change the length if it improves the text
- Maintain the original intent and key information
- Adapt the tone to be more professional or engaging as needed
- Return only the rewritten text, no explanations

Text to rewrite:"""

async def process_text_with_ai(text: str, prompt: str) -> str:
    if not llm:
        raise HTTPException(status_code=500, detail="AI service not available")
    try:
        messages = [
            SystemMessage(content=prompt),
            HumanMessage(content=text)
        ]
        response = llm.invoke(messages)
        return response.content.strip()
    except Exception as e:
        logger.error(f"Error processing text: {e}")
        raise HTTPException(status_code=500, detail=f"AI processing failed: {str(e)}")
