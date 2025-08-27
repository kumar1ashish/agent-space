from agent_space import agents, providers

llm = providers.get("openai")
agent = agents.manager_worker(llm, workers=["w1", "w2"])
print(agent.run("task").text)
