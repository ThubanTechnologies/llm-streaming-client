from typing import Dict, Any
from .http_client import HttpClient
from src.llm_streaming_client.config.config import CONFIG
from src.llm_streaming_client.adapter.exceptions import AudioTranscriptionException

class ConfigAudioAdapter(HttpClient):
    """Adapter to interact with the audio transcription microservice paths."""

    def __init__(self, base_url: str, timeout: int = CONFIG.TIMEOUT) -> None:
        super().__init__(timeout=timeout)
        self._config = CONFIG.config_audio_adapter
        self.base_url = base_url
    
    def transcribe_audio(self, audio_service: str, audio_url: str) -> Dict[str, Any]:
        """
        Sends an audio file to the transcription service and retrieves the transcription.
        """
        url = self.base_url + self._config["audio"]
        try:
            with open(audio_url, "rb") as audio_file:
                files = {"audio": (audio_url, audio_file, "audio/wav")}
                data = {"audio_service": audio_service}
                response = self._post(url, files=files, data=data)
                return response
        except Exception as e:
            raise AudioTranscriptionException(f"Failed to transcribe audio: {e}") from e
