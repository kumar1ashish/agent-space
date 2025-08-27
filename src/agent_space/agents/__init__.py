"""Agent patterns."""

from __future__ import annotations

from .autobuild import autobuild
from .base import Agent, AgentResult
from .multi.groupchat import groupchat
from .multi.manager_worker import manager_worker
from .multi.swarm import swarm
from .realtime.gemini_ws import gemini_ws
from .single.plan_act_reflect import plan_act_reflect
from .single.react import react
from .single.retrieve_chat import retrieve_chat

__all__ = [
    "Agent",
    "AgentResult",
    "react",
    "plan_act_reflect",
    "retrieve_chat",
    "groupchat",
    "manager_worker",
    "swarm",
    "gemini_ws",
    "autobuild",
]
