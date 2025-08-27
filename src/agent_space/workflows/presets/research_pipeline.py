"""Research pipeline workflow stub."""

from __future__ import annotations

from ..dag import DAG, Step


def research_pipeline() -> DAG:
    steps = [
        Step("search", lambda _: "results"),
        Step("read", lambda results: f"read {results}"),
        Step("draft", lambda text: f"draft from {text}"),
    ]
    return DAG(steps)


__all__ = ["research_pipeline"]
