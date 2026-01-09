# src/config.py

import os
from pydantic import BaseModel
from dotenv import load_dotenv

load_dotenv(override=True)


class OpenAIConfig(BaseModel):
    api_key: str = os.getenv("OPENAI_API_KEY")
    model: str = os.getenv("OPENAI_MODEL", "gpt-4o")
    temperature: float = float(os.getenv("OPENAI_TEMPERATURE", "0.7"))
    max_tokens: int = int(os.getenv("OPENAI_MAX_TOKENS", "800"))


openai_config = OpenAIConfig()

if not openai_config.api_key:
    raise RuntimeError("OPENAI_API_KEY not found in environment")
