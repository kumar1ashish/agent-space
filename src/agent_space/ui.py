"""Simple text UI for building agents and running them."""

from __future__ import annotations

from rich.console import Console
from rich.prompt import Prompt

from . import agents, providers
from .memory import VectorStore

console = Console()


def build_agent() -> agents.Agent:
    """Interactively construct an agent pattern."""

    pattern = Prompt.ask("Select pattern", choices=["groupchat", "retrieve_chat"])
    provider = Prompt.ask(
        "LLM provider", choices=["openai", "anthropic", "gemini"], default="openai"
    )
    llm = providers.get(provider)
    if pattern == "groupchat":
        names = Prompt.ask("Agent names (comma-separated)", default="a,b")
        agent_names = [name.strip() for name in names.split(",") if name.strip()]
        return agents.groupchat(llm, agents=agent_names)
    else:
        store = VectorStore()
        console.print("Enter documents for retrieval (blank line to finish):")
        idx = 1
        while True:
            doc = Prompt.ask(f"doc #{idx}", default="")
            if not doc:
                break
            store.add(str(idx), doc)
            idx += 1
        return agents.retrieve_chat(llm, store)


def interactive() -> None:
    """Interactive loop for the agent built by :func:`build_agent`."""

    agent = build_agent()
    console.print("[bold]Agent ready. Submit blank input to exit.[/bold]")
    while True:
        question = Prompt.ask("You", default="")
        if not question:
            break
        result = agent.run(question)
        console.print(f"[green]{result.text}[/green]")


__all__ = ["interactive", "build_agent"]
