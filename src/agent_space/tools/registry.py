"""Tool registry."""

from __future__ import annotations

from collections.abc import Callable
from typing import TypeVar

from .base import Tool

T = TypeVar("T", bound=Tool)

_REGISTRY: dict[str, Callable[[], Tool]] = {}


def register(name: str, factory: Callable[[], T]) -> None:
    """Register a tool factory under ``name``."""

    _REGISTRY[name] = factory


def get(name: str) -> Tool:
    """Retrieve a tool instance."""

    try:
        factory = _REGISTRY[name]
    except KeyError as exc:  # pragma: no cover - defensive
        raise ValueError(f"Unknown tool: {name}") from exc
    return factory()


def list_tools() -> list[str]:
    """Return the names of available tools."""

    return sorted(_REGISTRY)


__all__ = ["register", "get", "list_tools"]
