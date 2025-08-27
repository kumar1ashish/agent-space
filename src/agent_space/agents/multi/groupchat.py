"""Group chat orchestration stub."""

from __future__ import annotations

from collections.abc import Iterable

from ...providers import LLMClient
from ..base import Agent, AgentResult


class GroupChat(Agent):
    """Very small group chat that concatenates agent names."""

    def __init__(
        self,
        llm: LLMClient,
        agents: Iterable[str],
        tools: Iterable[object] | None = None,
    ) -> None:
        super().__init__(llm)
        self.agents = list(agents)
        self.tools = list(tools or [])

    def run(self, input: str | dict[str, str], **kwargs: object) -> AgentResult:
        user = input if isinstance(input, str) else input.get("content", "")
        prefix = ", ".join(self.agents)
        return super().run(f"{prefix}: {user}", **kwargs)


def groupchat(
    llm: LLMClient, agents: Iterable[str], tools: Iterable[object] | None = None
) -> GroupChat:
    return GroupChat(llm, agents, tools)


__all__ = ["groupchat", "GroupChat"]
