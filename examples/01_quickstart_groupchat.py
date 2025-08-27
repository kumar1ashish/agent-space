from agent_space import agents, providers

llm = providers.get("openai")
gc = agents.groupchat(llm, agents=["planner", "researcher", "reviewer"])
print(gc.run("hello").text)
