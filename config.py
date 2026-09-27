from __future__ import annotations

import os

from dotenv import load_dotenv

load_dotenv()


def get_env(name: str, required: bool = True) -> str | None:
    value = os.getenv(name)

    if required and not value:
        raise RuntimeError(f"Missing required environment variable: {name}")

    return value


def get_model_config() -> dict[str, str]:
    return {
        "gemini": os.getenv(
            "GEMINI_MODEL",
            "gemini-3.8-flash",
        ),
        "groq_reasoning": os.getenv(
            "GROQ_REASONING_MODEL",
            "openai/gpt-oss-120b",
        ),
        "embedding": os.getenv(
            "EMBEDDING_MODEL",
            "BAAI/bge-small-en-v1.5",
        ),
    }
