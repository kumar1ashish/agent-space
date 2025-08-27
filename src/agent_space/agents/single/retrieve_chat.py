"""RetrieveChat stub pattern."""

from __future__ import annotations

from ...memory import VectorStore
from ...providers import LLMClient
from ..base import Agent, AgentResult


class RetrieveChat(Agent):
    """Very small wrapper that queries a :class:`VectorStore`."""

    def __init__(self, llm: LLMClient, store: VectorStore) -> None:
        super().__init__(llm)
        self.store = store

    def run(self, input: str | dict[str, str], **kwargs: object) -> AgentResult:
        query = input if isinstance(input, str) else input.get("content", "")
        docs = self.store.query(query)
        context = docs[0] if docs else "no documents"
        prompt = f"{context}\nQuestion: {query}"
        return super().run(prompt, **kwargs)


def retrieve_chat(llm: LLMClient, store: VectorStore) -> RetrieveChat:
    return RetrieveChat(llm, store)


__all__ = ["retrieve_chat", "RetrieveChat"]
