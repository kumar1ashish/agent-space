"""Configuration helpers."""

from __future__ import annotations

import os
from dataclasses import dataclass


@dataclass
class Settings:
    """Runtime settings loaded from environment variables."""

    openai_api_key: str | None = None
    anthropic_api_key: str | None = None
    gemini_api_key: str | None = None

    @classmethod
    def from_env(cls) -> Settings:
        return cls(
            openai_api_key=os.getenv("OPENAI_API_KEY"),
            anthropic_api_key=os.getenv("ANTHROPIC_API_KEY"),
            gemini_api_key=os.getenv("GEMINI_API_KEY"),
        )


def get_settings() -> Settings:
    """Return settings from environment."""

    return Settings.from_env()


__all__ = ["Settings", "get_settings"]
