from agent_space import agents, memory


def test_retrieve_chat(llm) -> None:
    store = memory.VectorStore()
    store.add("1", "onboarding sop")
    rc = agents.retrieve_chat(llm, store)
    out = rc.run("onboarding").text
    assert "onboarding" in out.lower()
