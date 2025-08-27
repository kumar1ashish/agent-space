"""Realtime Gemini WebSocket stub."""

from __future__ import annotations

import threading

import uvicorn
from fastapi import FastAPI, WebSocket
from starlette.websockets import WebSocketDisconnect


class GeminiRealtimeServer:
    """Tiny FastAPI server that echoes messages over WebSocket."""

    def __init__(
        self, model: str = "gemini-pro", host: str = "127.0.0.1", port: int = 8000
    ) -> None:
        self.model = model
        self.host = host
        self.port = port
        self.app = FastAPI()

        @self.app.websocket("/ws")
        async def ws_endpoint(
            websocket: WebSocket,
        ) -> None:  # pragma: no cover - network
            await websocket.accept()
            try:
                while True:
                    data = await websocket.receive_text()
                    await websocket.send_text(data[::-1])
            except WebSocketDisconnect:
                pass

    def start(self) -> None:  # pragma: no cover - network
        config = uvicorn.Config(
            self.app, host=self.host, port=self.port, log_level="error"
        )
        server = uvicorn.Server(config)
        thread = threading.Thread(target=server.run, daemon=True)
        thread.start()
        self._server = server
        self._thread = thread


def gemini_ws(model: str = "gemini-pro") -> GeminiRealtimeServer:
    return GeminiRealtimeServer(model=model)


__all__ = ["GeminiRealtimeServer", "gemini_ws"]
