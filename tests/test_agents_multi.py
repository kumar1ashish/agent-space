from agent_space import agents


def test_groupchat(llm) -> None:
    gc = agents.groupchat(llm, agents=["planner", "researcher", "reviewer"])
    out = gc.run("hi").text
    assert "planner" in out and "reviewer" in out
