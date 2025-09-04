from typing import Dict, Any
from .http_client import HttpClient
import mimetypes
import os
from ..config.config import CONFIG
from ..adapter.exceptions import AudioTranscriptionException


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
            mime_type, _ = mimetypes.guess_type(audio_url)
            if not mime_type:
                mime_type = "application/octet-stream"
            with open(audio_url, "rb") as audio_file:
                files = {"audio": (audio_url, audio_file, mime_type)}
                data = {"audio_service": audio_service}
                response = self._post(url, files=files, data=data)

                if response.get("success") and "response" in response:
                    audio_response = response["response"]
                    if "text" in audio_response:
                        response["response"] = audio_response["text"]
                        return response
                    else:
                        return response
                else:
                    return response

        except Exception as e:
            raise AudioTranscriptionException(f"Failed to transcribe audio: {e}") from e
