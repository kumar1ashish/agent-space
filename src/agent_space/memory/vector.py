"""Very small vector store stub."""

from __future__ import annotations


class VectorStore:
    """In-memory vector store used for tests."""

    def __init__(self) -> None:
        self._store: dict[str, str] = {}

    def add(self, doc_id: str, text: str) -> None:
        self._store[doc_id] = text

    def query(self, query: str) -> list[str]:  # pragma: no cover - trivial
        return [text for text in self._store.values() if query.lower() in text.lower()]


__all__ = ["VectorStore"]
