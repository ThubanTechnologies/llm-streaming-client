import socketio
from typing import List, Dict, Any, Optional
from src.llm_streaming_client.config.config import CONFIG

class SocketAdapter:
    """Adapter to interact with the Socket.IO server."""

    def __init__(self, base_url:str, timeout: int = CONFIG.TIMEOUT) -> None:
        """
        Initialize the Socket.IO adapter.

        Args:
            namespace (str): The namespace to connect to.
            timeout (int): Maximum wait time for the connection (in seconds).
        """
        self.sio = socketio.Client(reconnection_attempts=CONFIG.RECONNECT_ATTEMPTS, request_timeout=timeout)
        self.namespace = CONFIG.SOCKET_NAMESPACE
        self.timeout = timeout
        self.base_url = base_url

    def send_messages(
        self,
        messages: List[Dict[str, Any]],
        llm: str = "openai",
        model: str = "gpt-4o-mini",
    ) -> None:
        """
        Sends a list of messages to the Socket.IO server and streams the response tokens.

        Args:
            messages (list): A list of messages to send. Each message should be a dictionary with 'id', 'content', 'type', and 'timestamp'.
            llm (str, optional): The LLM provider name. Defaults to "openai".
            model (str, optional): The model name. Defaults to "gpt-4o-mini".
        """
        @self.sio.on("response_message", namespace=self.namespace)
        def on_response_message(data):
            content = data.get("content", "")
            finished = data.get("finished", False)
            print(content, end="", flush=True)
            if finished:
                self.sio.disconnect()

        @self.sio.on("error", namespace=self.namespace)
        def on_error(data):
            print(f"Error: {data}")
            self.sio.disconnect()

        try:
            self.sio.connect(self.base_url, namespaces=[self.namespace])

            message_payload = {
                "messages": messages,
                "llm": llm,
                "model": model,
                "actionKey": "default",
            }

            self.sio.emit("send_message", message_payload, namespace=self.namespace)
            self.sio.wait()
        except Exception as e:
            print(f"An error occurred: {e}")
        finally:
            if self.sio.connected:
                self.sio.disconnect()