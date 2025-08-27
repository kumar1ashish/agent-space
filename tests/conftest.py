"""Test fixtures."""

from __future__ import annotations

import pytest

from agent_space import providers


@pytest.fixture
def llm() -> providers.LLMClient:
    return providers.get("openai")
