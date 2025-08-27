"""Agent wrappers."""

from __future__ import annotations

from collections.abc import Iterator
from dataclasses import dataclass
from typing import Any

from ..providers import LLMChunk, LLMClient


@dataclass
class AgentResult:
    """Result returned by :meth:`Agent.run`."""

    text: str
    messages: list[dict[str, str]]


class Agent:
    """Tiny agent wrapper around an :class:`LLMClient`."""

    def __init__(self, llm: LLMClient) -> None:
        self.llm = llm

    def run(self, input: str | dict[str, str], **kwargs: Any) -> AgentResult:
        messages = (
            [input] if isinstance(input, dict) else [{"role": "user", "content": input}]
        )
        response = self.llm.generate(messages, **kwargs)
        messages.append({"role": "assistant", "content": response.text})
        return AgentResult(text=response.text, messages=messages)

    def run_stream(
        self, input: str, **kwargs: Any
    ) -> Iterator[LLMChunk]:  # pragma: no cover - trivial
        messages = [{"role": "user", "content": input}]
        yield from self.llm.stream(messages, **kwargs)


__all__ = ["Agent", "AgentResult"]
