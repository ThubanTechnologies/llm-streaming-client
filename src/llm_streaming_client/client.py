from typing import BinaryIO, Union, List, Dict, Any, Optional, Callable
from .adapter.http_client import HttpClient
from .dtos.request import POSTFile, GETFile, PUTFile, DELETEFile, GETStructure
from .dtos.response import FileEntity
from .adapter.server_request_adapter import ServerRequestAdapter
from .adapter.config_audio_adapter import ConfigAudioAdapter
from .adapter.config_adapter import ConfigAdapter
from .adapter.socket_client import SocketAdapter
from typing import Dict, Any, Optional
from src.llm_streaming_client.config.config import CONFIG

class LLMStreamingClient:
    """Simplified client for the llm_streaming."""

    def __init__(self, base_url: Optional[str], timeout: int = CONFIG.TIMEOUT) -> None:
        """
        Initialize the client.
        
        Args:
            base_url: Base URL of the service
            timeout: Maximum wait time for requests
        """
        self.base_url = base_url if base_url else CONFIG.BASE_URL
        self.config_adapter = ConfigAdapter(timeout=timeout, base_url=self.base_url)
        self.config_audio_adapter = ConfigAudioAdapter(timeout=timeout, base_url=self.base_url)
        self.server_request_adapter = ServerRequestAdapter(timeout=timeout, base_url=self.base_url)
        self.socket_adapter = SocketAdapter(timeout=timeout, base_url=self.base_url)

    def get_status(self) -> Dict[str, Any]:
        """
        Get the status of the service.

        Returns:
            Dictionary with the status information.
        """
        return self.config_adapter.status()

    def get_models(self) -> Dict[str, Any]:
        """
        Get the list of available models.

        Returns:
            Dictionary with the available models.
        """
        return self.config_adapter.get_available_models()

    def get_llms(self) -> Dict[str, Any]:
        """
        Get the list of available LLMs.

        Returns:
            Dictionary with the available LLMs.
        """
        return self.config_adapter.get_available_llms()

    def get_prompts(self) -> List[Dict[str, Any]]:
        """
        Get the list of available prompts with their metadata.

        Returns:
            List of dictionaries containing prompt metadata.
        """
        return self.config_adapter.get_available_prompts()
    
    def transcribe_audio(self, audio_service: str, audio_url: str) -> Dict[str, Any]:
        """
        Transcribe an audio file using the specified audio service.

        Args:
            audio_service: The name of the audio service to use.
            audio_file: The audio file in binary format.

        Returns:
            A dictionary containing the transcription result.
        """
        return self.config_audio_adapter.transcribe_audio(audio_service, audio_url)
    
    def handle_request(
        self,
        text: Optional[str],
        action_key: str,
        llm_name: Optional[str] = None,
        model_name: Optional[str] = None,
        image_object: Optional[Any] = None,
    ) -> Dict[str, Any]:
        """
        Handle a request to the LLM service.

        Args:
            text: The input text for the request.
            action_key: The action key to determine the type of request.
            llm_name: The name of the LLM to use (default: "openai").
            model_name: The name of the model to use (default: "gpt-4o-mini").
            image_object: Optional image object for the request.

        Returns:
            A dictionary containing the response from the LLM service.
        """
        return self.server_request_adapter.handle_request(
            text=text,
            action_key=action_key,
            llm_name=llm_name,
            model_name=model_name,
            image_object=image_object,
        )
    
    def send_messages_via_socket(
        self,
        messages: List[Dict[str, Any]],
        llm: Optional[str] = "openai",
        model: Optional[str] = "gpt-4o-mini",
    ) -> None:
        """
        Sends messages to the Socket.IO server using the socket adapter.

        Args:
            url (str): The URL of the Socket.IO server.
            messages (list): A list of messages to send.
            llm (str, optional): The LLM provider name. Defaults to "openai".
            model (str, optional): The model name. Defaults to "gpt-4o-mini".
        """
        self.socket_adapter.send_messages(messages, llm, model)
    