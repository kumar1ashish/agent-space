"""Manager/worker pattern stub."""

from __future__ import annotations

from collections.abc import Iterable

from ...providers import LLMClient
from ..base import Agent, AgentResult


class ManagerWorker(Agent):
    """Simple manager that delegates to worker names."""

    def __init__(self, llm: LLMClient, workers: Iterable[str]) -> None:
        super().__init__(llm)
        self.workers = list(workers)

    def run(self, input: str | dict[str, str], **kwargs: object) -> AgentResult:
        prompt = input if isinstance(input, str) else input.get("content", "")
        tasks = "; ".join(self.workers)
        return super().run(f"{tasks}: {prompt}", **kwargs)


def manager_worker(llm: LLMClient, workers: Iterable[str]) -> ManagerWorker:
    return ManagerWorker(llm, workers)


__all__ = ["manager_worker", "ManagerWorker"]
