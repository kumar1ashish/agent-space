"""Provider factory registry."""

from __future__ import annotations

from collections.abc import Callable

from .anthropic import AnthropicClient
from .base import LLMClient
from .gemini import GeminiClient
from .openai import OpenAIClient

_FACTORIES: dict[str, Callable[..., LLMClient]] = {
    "openai": OpenAIClient,
    "anthropic": AnthropicClient,
    "gemini": GeminiClient,
}


def get(name: str, **kwargs: object) -> LLMClient:
    """Return an initialized provider client."""

    try:
        factory = _FACTORIES[name]
    except KeyError as exc:  # pragma: no cover - defensive
        raise ValueError(f"Unknown provider: {name}") from exc
    return factory(**kwargs)


__all__ = ["get"]
