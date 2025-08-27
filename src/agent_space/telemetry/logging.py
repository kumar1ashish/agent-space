"""Logging helpers."""

from __future__ import annotations

import logging
import uuid

_logger = logging.getLogger("agent_space")


def get_logger(run_id: str | None = None) -> logging.Logger:
    """Return a child logger with ``run_id``."""

    run_id = run_id or str(uuid.uuid4())
    return _logger.getChild(run_id)


__all__ = ["get_logger"]
