from agent_space import agents, memory, providers

llm = providers.get("openai")
store = memory.VectorStore()
store.add("1", "hello world doc")
rc = agents.retrieve_chat(llm, store)
print(rc.run("hello?").text)
