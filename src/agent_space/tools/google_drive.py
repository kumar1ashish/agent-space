"""Google Drive stub tool."""

from __future__ import annotations

from typing import Any

from pydantic import BaseModel

from .base import Tool, ToolResult
from .registry import register


class GoogleDriveArgs(BaseModel):
    file_id: str


class GoogleDrive:
    name = "google_drive"
    description = "Read file from drive"
    Args: type[BaseModel] = GoogleDriveArgs

    def __call__(self, **kwargs: Any) -> ToolResult:  # pragma: no cover - simple
        args = GoogleDriveArgs(**kwargs)
        return ToolResult(text=f"contents of {args.file_id}")


def google_drive() -> Tool:
    return GoogleDrive()


register("google_drive", google_drive)

__all__ = ["google_drive", "GoogleDrive", "GoogleDriveArgs"]
