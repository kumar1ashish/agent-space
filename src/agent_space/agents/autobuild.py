"""AutoBuild facade stub."""

from __future__ import annotations

from ..providers import LLMClient
from .base import Agent


def autobuild(llm: LLMClient) -> Agent:
    """Return a simple agent; placeholder for AG2 AutoBuild."""

    return Agent(llm)


__all__ = ["autobuild"]
