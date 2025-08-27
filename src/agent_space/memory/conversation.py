"""Conversation memory."""

from __future__ import annotations

Message = tuple[str, str]


class ConversationMemory:
    """Very small conversation memory with token-window trimming."""

    def __init__(self, max_messages: int = 10) -> None:
        self.max_messages = max_messages
        self._messages: list[Message] = []

    def remember(self, role: str, content: str) -> None:
        self._messages.append((role, content))
        if len(self._messages) > self.max_messages:
            self._messages.pop(0)

    def recall(self) -> list[Message]:
        return list(self._messages)

    def clear(self) -> None:
        self._messages.clear()


__all__ = ["ConversationMemory", "Message"]
