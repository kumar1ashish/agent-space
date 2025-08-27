"""Swarm helper stub."""

from __future__ import annotations

from ...providers import LLMClient
from ..base import Agent


def swarm(llm: LLMClient) -> Agent:
    """Return a basic agent representing a swarm."""

    return Agent(llm)


__all__ = ["swarm"]
