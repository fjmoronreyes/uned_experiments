# src/config_openai.py

from openai import OpenAI
from config import openai_config


class OpenAIClient:
    def __init__(self):
        self.client = OpenAI(api_key=openai_config.api_key)

    def generate_text(self, prompt: str) -> str:
        response = self.client.chat.completions.create(
            model=openai_config.model,
            messages=[
                {"role": "system", "content": "You are a neutral, encyclopedic narrator."},
                {"role": "user", "content": prompt},
            ],
            temperature=openai_config.temperature,
            max_tokens=openai_config.max_tokens,
        )
        return response.choices[0].message.content.strip()
