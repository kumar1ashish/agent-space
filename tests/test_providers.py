from agent_space import providers


def test_provider_generate(llm: providers.LLMClient) -> None:
    resp = llm.generate([{"role": "user", "content": "hi"}])
    assert resp.text == "hi"
    assert resp.total_tokens == resp.prompt_tokens + resp.completion_tokens


def test_registry_get() -> None:
    client = providers.get("anthropic")
    assert client.generate([{"role": "user", "content": "hi"}]).text == "HI"
