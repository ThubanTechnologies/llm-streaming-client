import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.llm_streaming_client.client import LLMStreamingClient
from src.llm_streaming_client.config.config import CONFIG


def token_printer(content: str, finished: bool):
    print(content, end="", flush=True)
    if finished:
        print("\n--- STREAM FINISHED ---")


if __name__ == "__main__":
    base_url = CONFIG.BASE_URL
    timeout = CONFIG.TIMEOUT
    client = LLMStreamingClient(base_url, timeout)
    action_key = "assistant"
    session_id = "session12347"

    texts = [
        "Hola, me llamo Pepito.",
        "¿Cómo me llamo?",
    ]
    for text in texts:
        client.send_messages_via_socket(
            text=text,
            on_token=token_printer,
            session_id=session_id,
            action_key=action_key,
        )
