"""JSON I/O utilities."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


def read_json(path: str | Path) -> Any:
    """Read JSON from ``path``."""

    with Path(path).open("r", encoding="utf-8") as fh:
        return json.load(fh)


def write_json(path: str | Path, data: Any) -> None:
    """Write ``data`` as JSON to ``path``."""

    with Path(path).open("w", encoding="utf-8") as fh:
        json.dump(data, fh)


__all__ = ["read_json", "write_json"]
