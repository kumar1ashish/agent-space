"""ReAct pattern stub."""

from __future__ import annotations

from ...providers import LLMClient
from ..base import Agent


def react(llm: LLMClient) -> Agent:
    """Return a simple :class:`Agent` for the ReAct pattern."""

    return Agent(llm)


__all__ = ["react"]
