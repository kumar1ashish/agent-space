"""Tracing helpers with optional OpenTelemetry."""

from __future__ import annotations

from collections.abc import Iterator
from contextlib import contextmanager

try:  # pragma: no cover - optional
    from opentelemetry import trace
except Exception:  # pragma: no cover - optional
    trace = None  # type: ignore[assignment]


@contextmanager
def start_span(name: str) -> Iterator[None]:
    """Start a tracing span if OpenTelemetry is installed."""

    if trace is None:
        yield
    else:  # pragma: no cover - optional
        tracer = trace.get_tracer("agent_space")
        with tracer.start_as_current_span(name):
            yield


__all__ = ["start_span"]
