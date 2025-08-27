"""Retry utilities."""

from __future__ import annotations

import time
from collections.abc import Callable
from typing import TypeVar

T = TypeVar("T")


def retry(fn: Callable[[], T], attempts: int = 3, delay: float = 0.01) -> T:
    """Execute ``fn`` with simple retries."""

    for i in range(attempts):
        try:
            return fn()
        except Exception:
            if i == attempts - 1:
                raise
            time.sleep(delay)
    raise RuntimeError("unreachable")


__all__ = ["retry"]
