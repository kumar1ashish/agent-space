from agent_space import agents

server = agents.gemini_ws()
# server.start()  # Uncomment to start server
print("Server ready", server.host)
