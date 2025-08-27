"""Tests for the interactive UI helpers."""

from __future__ import annotations

from agent_space.ui import build_agent


def test_build_agent_groupchat(monkeypatch) -> None:
    responses = iter(["groupchat", "openai", "alice,bob"])
    monkeypatch.setattr(
        "agent_space.ui.Prompt.ask", lambda *args, **kwargs: next(responses)
    )
    agent = build_agent()
    assert agent.agents == ["alice", "bob"]


def test_build_agent_retrieve_chat(monkeypatch) -> None:
    responses = iter(["retrieve_chat", "openai", "doc one", ""])
    monkeypatch.setattr(
        "agent_space.ui.Prompt.ask", lambda *args, **kwargs: next(responses)
    )
    agent = build_agent()
    assert agent.store._store == {"1": "doc one"}
