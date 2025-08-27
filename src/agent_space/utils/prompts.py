"""Prompt helpers."""

from __future__ import annotations


def format_prompt(template: str, **kwargs: object) -> str:
    """Format ``template`` with ``kwargs``."""

    return template.format(**kwargs)


__all__ = ["format_prompt"]
