"""Google search stub."""

from __future__ import annotations

from typing import Any

from pydantic import BaseModel

from .base import Tool, ToolResult
from .registry import register


class GoogleSearchArgs(BaseModel):
    query: str


class GoogleSearch:
    name = "google_search"
    description = "Return top search result"
    Args: type[BaseModel] = GoogleSearchArgs

    def __call__(self, **kwargs: Any) -> ToolResult:  # pragma: no cover - simple
        args = GoogleSearchArgs(**kwargs)
        return ToolResult(text=f"search results for {args.query}")


def google_search() -> Tool:
    return GoogleSearch()


register("google_search", google_search)

__all__ = ["google_search", "GoogleSearch", "GoogleSearchArgs"]
