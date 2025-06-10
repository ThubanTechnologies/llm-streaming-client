# llm-streaming-client

This project is a simplified Python client library for interacting with the [LLM_Streaming](https://github.com/ThubanTech/llm-streaming) service. It allows users to easily access LLM endpoints for text, audio, and image processing, including chat, summarization, extraction, and audio transcription, via HTTP and Socket.IO.

## Project Structure

- `src/llm_streaming_client/`: Contains the client's source code.
  - `client.py`: Main entry point. Defines the `LLMStreamingClient` class with high-level methods to interact with the LLM_Streaming service.
  - `adapter/`: Contains adapters for HTTP, audio, config, and socket communication.
  - `dtos/`: Data Transfer Objects for structured input and output.
  - `enums/`: Enumerations for action keys, language, etc.
  - `config/`: Configuration management for the client.
- `examples/`: Example scripts demonstrating usage of the client for different scenarios.

## Installation

To install the client, clone the repository and use `pip` to install the dependencies:

```bash
git clone https://github.com/ThubanTech/llm-streaming-client.git
cd llm-streaming-client
pip install -e .
```

Or install directly from GitHub (for a specific branch):
```bash
pip install git+https://github.com/ThubanTech/llm-streaming-client.git@main#egg=llm_streaming-client
```
## Usage

Below are basic examples of how to use the LLMStreamingClient for different LLM_Streaming features.

- Get Service Status
```python
from src.llm_streaming_client.client import LLMStreamingClient
from src.llm_streaming_client.config.config import CONFIG

client = LLMStreamingClient(CONFIG.BASE_URL, CONFIG.TIMEOUT)
status = client.get_status()
print("Service Status:", status)
```

- Transcribe Audio
```python
from src.llm_streaming_client.client import LLMStreamingClient
from src.llm_streaming_client.config.config import CONFIG
import os

client = LLMStreamingClient(CONFIG.BASE_URL, CONFIG.TIMEOUT)
audio_service = "openai"
audio_file_path = os.path.join(os.path.dirname(__file__), "prueba_audio.wav")
result = client.transcribe_audio(audio_service, audio_file_path)
print("Transcription Result:", result)
```

- Send Messages via Socket
```python
from src.llm_streaming_client.client import LLMStreamingClient
from src.llm_streaming_client.config.config import CONFIG

client = LLMStreamingClient(CONFIG.BASE_URL, CONFIG.TIMEOUT)
messages = [
    {"id": "1", "content": "Hola, me llamo Pepito", "type": "user", "timestamp": "2025-04-09T12:00:00Z"},
    {"id": "2", "content": "¿Cómo me llamo?", "type": "user", "timestamp": "2025-04-09T12:01:00Z"},
]
client.send_messages_via_socket(messages)
```

- Summarization, Extraction etc
```python
from src.llm_streaming_client.client import LLMStreamingClient
from src.llm_streaming_client.config.config import CONFIG

client = LLMStreamingClient(CONFIG.BASE_URL, CONFIG.TIMEOUT)
response = client.handle_request(
    text="La mañana comenzó con un cielo nublado...",
    action_key="summarize",
    llm_name="openai",
    model_name="gpt-4o-mini",
)
print("Response from handle_request (summarize):", response)
```

## Contributions

Contributions are welcome. If you wish to contribute, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.