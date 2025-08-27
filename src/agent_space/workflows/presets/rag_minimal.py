"""RAG minimal workflow stub."""

from __future__ import annotations

from ..dag import DAG, Step


def rag_minimal() -> DAG:
    steps = [
        Step("retrieve", lambda _: "docs"),
        Step("answer", lambda docs: f"answer from {docs}"),
    ]
    return DAG(steps)


__all__ = ["rag_minimal"]
