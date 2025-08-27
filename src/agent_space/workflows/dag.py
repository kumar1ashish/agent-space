"""Lightweight workflow DAG."""

from __future__ import annotations

from collections.abc import Callable, Iterator
from dataclasses import dataclass
from typing import Any


@dataclass
class Step:
    """Workflow step."""

    name: str
    func: Callable[[Any], Any]

    def run(self, data: Any) -> Any:
        return self.func(data)


class DAG:
    """A minimal directed acyclic workflow."""

    def __init__(self, steps: list[Step]) -> None:
        self.steps = steps

    def run(self, initial: Any = None) -> Iterator[dict[str, Any]]:
        data = initial
        for step in self.steps:
            data = step.run(data)
            yield {"step": step.name, "output": data}


__all__ = ["Step", "DAG"]
