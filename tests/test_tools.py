from agent_space import tools


def test_tools_registry() -> None:
    names = tools.list_tools()
    assert "browser" in names
    tool = tools.get("browser")
    assert tool(url="https://example.com").text.startswith("fetched")
