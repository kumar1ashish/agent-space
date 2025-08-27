"""Anthropic provider stub."""

from __future__ import annotations

from collections.abc import Iterator
from typing import Any

from .base import LLMChunk, LLMResponse


class AnthropicClient:
    """Simple echo client used for tests."""

    def __init__(self, model: str = "claude-3-haiku") -> None:
        self.model = model

    def generate(self, messages: list[dict[str, str]], **_: Any) -> LLMResponse:
        text = messages[-1]["content"] if messages else ""
        length = len(text)
        return LLMResponse(
            text=text.upper(), prompt_tokens=length, completion_tokens=length
        )

    def stream(self, messages: list[dict[str, str]], **_: Any) -> Iterator[LLMChunk]:
        yield LLMChunk(text=self.generate(messages).text)


__all__ = ["AnthropicClient"]
