"""Command line interface."""

from __future__ import annotations

import typer

from . import agents, providers, tools
from .memory import VectorStore
from .ui import interactive

app = typer.Typer(help="Agent Space CLI")


@app.command()
def list(category: str) -> None:
    """List available components."""

    if category == "tools":
        typer.echo(", ".join(tools.list_tools()))
    elif category == "providers":
        typer.echo("openai, anthropic, gemini")
    elif category == "agents":
        typer.echo("groupchat, retrieve_chat")
    else:
        raise typer.BadParameter("unknown category")


@app.command()
def run(pattern: str, input: str, provider: str = "openai") -> None:
    """Run a simple pattern."""

    llm = providers.get(provider)
    agent: agents.Agent
    if pattern == "groupchat":
        agent = agents.groupchat(llm, agents=["a", "b"])
    elif pattern == "retrievechat":
        store = VectorStore()
        store.add("1", "dummy document")
        agent = agents.retrieve_chat(llm, store)
    else:
        raise typer.BadParameter("unknown pattern")
    typer.echo(agent.run(input).text)


@app.command()
def ui() -> None:
    """Launch a simple interactive UI for building and running agents."""

    interactive()


__all__ = ["app"]
