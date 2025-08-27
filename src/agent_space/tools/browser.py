"""Browser tool stub."""

from __future__ import annotations

from typing import Any

from pydantic import BaseModel

from .base import Tool, ToolResult
from .registry import register


class BrowserArgs(BaseModel):
    url: str


class Browser:
    name = "browser"
    description = "Fetch a URL"
    Args: type[BaseModel] = BrowserArgs

    def __call__(self, **kwargs: Any) -> ToolResult:  # pragma: no cover - simple
        args = BrowserArgs(**kwargs)
        return ToolResult(text=f"fetched {args.url}")


def browser() -> Tool:
    return Browser()


register("browser", browser)

__all__ = ["browser", "Browser", "BrowserArgs"]
