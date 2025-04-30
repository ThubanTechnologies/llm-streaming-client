import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.llm_streaming_client.config.config import CONFIG
from src.llm_streaming_client.client import LLMStreamingClient

def main():
    base_url = CONFIG.BASE_URL
    timeout = CONFIG.TIMEOUT

    client = LLMStreamingClient(base_url, timeout)

    audio_service = "openai" 
    audio_file_path = os.path.join(os.path.dirname(__file__), "prueba_audio.wav")
    result = client.transcribe_audio(audio_service, audio_file_path)
    print("Transcription Result:", result)

if __name__ == "__main__":
    main()