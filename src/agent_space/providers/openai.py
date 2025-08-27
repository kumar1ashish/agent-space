"""OpenAI provider stub."""

from __future__ import annotations

from collections.abc import Iterator
from typing import Any

from .base import LLMChunk, LLMResponse


class OpenAIClient:
    """Very small OpenAI-like client used for tests."""

    def __init__(self, model: str = "gpt-4o-mini") -> None:
        self.model = model

    def generate(self, messages: list[dict[str, str]], **_: Any) -> LLMResponse:
        text = messages[-1]["content"] if messages else ""
        length = len(text)
        return LLMResponse(text=text, prompt_tokens=length, completion_tokens=length)

    def stream(self, messages: list[dict[str, str]], **_: Any) -> Iterator[LLMChunk]:
        yield LLMChunk(text=self.generate(messages).text)


__all__ = ["OpenAIClient"]
