"""Plan-Act-Reflect pattern stub."""

from __future__ import annotations

from ...providers import LLMClient
from ..base import Agent


def plan_act_reflect(llm: LLMClient) -> Agent:
    """Return a basic agent implementing plan-act-reflect."""

    return Agent(llm)


__all__ = ["plan_act_reflect"]
