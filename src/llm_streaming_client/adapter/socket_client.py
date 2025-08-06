import socketio
from ..config.config import CONFIG
from ..dtos.input import StreamingInputDTO
from ..adapter.exceptions import SocketCommunicationException


class SocketAdapter:
    """Adapter to interact with the Socket.IO server using StreamingInputDTO."""

    def __init__(self, base_url: str, timeout: int = CONFIG.TIMEOUT) -> None:
        """
        Initialize the Socket.IO adapter.

        Args:
            base_url: The base URL to connect to.
            timeout: Maximum wait time for the connection (in seconds).
        """
        self.sio = socketio.Client(
            reconnection_attempts=CONFIG.RECONNECT_ATTEMPTS, request_timeout=timeout
        )
        self.namespace = CONFIG.SOCKET_NAMESPACE
        self.timeout = timeout
        self.base_url = base_url

    def send_messages(self, dto: StreamingInputDTO) -> None:
        """
        Sends a StreamingInputDTO to the Socket.IO server and streams the response tokens.

        Args:
            dto: A StreamingInputDTO containing messages, llm_name, model_name, action_key, language, etc.
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

            messages_payload = [
                {
                    "id": msg.id,
                    "content": msg.content,
                    "type": msg.type.value,
                    "timestamp": msg.timestamp,
                }
                for msg in dto.messages
            ]

            payload = {
                "messages": messages_payload,
                "llm_name": dto.llm_name,
                "model_name": dto.model_name,
                "action_key": dto.action_key.value,
                "language": dto.language.value,
            }
            if dto.image_object:
                payload["image_object"] = dto.image_object

            self.sio.emit("send_message", payload, namespace=self.namespace)
            self.sio.wait()

        except Exception as e:
            raise SocketCommunicationException(error=e)
        finally:
            if self.sio.connected:
                self.sio.disconnect()
