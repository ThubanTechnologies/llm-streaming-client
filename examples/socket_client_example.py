import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.llm_streaming_client.client import LLMStreamingClient
from src.llm_streaming_client.config.config import CONFIG

if __name__ == "__main__":
    base_url = CONFIG.BASE_URL
    timeout = CONFIG.TIMEOUT
    client = LLMStreamingClient(base_url, timeout)
    messages = [
        {"id": "1", "content": "Hola, me llamo Pepito", "type": "user", "timestamp": "2025-04-09T12:00:00Z"},
        {"id": "2", "content": "¿Cómo me llamo?", "type": "user", "timestamp": "2025-04-09T12:01:00Z"},
    ]
    client.send_messages_via_socket(messages)