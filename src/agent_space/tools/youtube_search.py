"""YouTube search stub."""

from __future__ import annotations

from typing import Any

from pydantic import BaseModel

from .base import Tool, ToolResult
from .registry import register


class YouTubeSearchArgs(BaseModel):
    query: str


class YouTubeSearch:
    name = "youtube_search"
    description = "Search YouTube videos"
    Args: type[BaseModel] = YouTubeSearchArgs

    def __call__(self, **kwargs: Any) -> ToolResult:  # pragma: no cover - simple
        args = YouTubeSearchArgs(**kwargs)
        return ToolResult(text=f"videos for {args.query}")


def youtube_search() -> Tool:
    return YouTubeSearch()


register("youtube_search", youtube_search)

__all__ = ["youtube_search", "YouTubeSearch", "YouTubeSearchArgs"]
