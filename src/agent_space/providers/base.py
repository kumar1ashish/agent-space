"""Provider base protocols."""

from __future__ import annotations

from collections.abc import Iterator
from dataclasses import dataclass
from typing import Any, Protocol


@dataclass
class LLMResponse:
    """A simple language model response."""

    text: str
    prompt_tokens: int = 0
    completion_tokens: int = 0

    @property
    def total_tokens(self) -> int:
        return self.prompt_tokens + self.completion_tokens


@dataclass
class LLMChunk:
    """Chunk of streamed LLM output."""

    text: str


class LLMClient(Protocol):
    """Protocol for language model clients."""

    def generate(self, messages: list[dict[str, str]], **kwargs: Any) -> LLMResponse:
        """Generate a completion from messages."""

    def stream(
        self, messages: list[dict[str, str]], **kwargs: Any
    ) -> Iterator[LLMChunk]:
        """Stream a completion from messages."""


__all__ = ["LLMClient", "LLMResponse", "LLMChunk"]
