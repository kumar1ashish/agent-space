"""Tool base abstractions."""

from __future__ import annotations

from typing import Any, Protocol

from pydantic import BaseModel


class ToolResult(BaseModel):
    """Simple tool result."""

    text: str


class Tool(Protocol):
    """Protocol for tools."""

    name: str
    description: str
    Args: type[BaseModel]

    def __call__(self, **kwargs: Any) -> ToolResult: ...


__all__ = ["Tool", "ToolResult"]
