from agent_space import agents


def test_react(llm) -> None:
    agent = agents.react(llm)
    assert agent.run("hello").text == "hello"
