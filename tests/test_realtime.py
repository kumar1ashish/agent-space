from fastapi.testclient import TestClient

from agent_space import agents


def test_realtime_ws() -> None:
    server = agents.gemini_ws()
    client = TestClient(server.app)
    with client.websocket_connect("/ws") as ws:
        ws.send_text("abc")
        assert ws.receive_text() == "cba"
