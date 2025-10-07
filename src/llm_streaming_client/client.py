from typing import BinaryIO, Union, List, Dict, Any, Optional, Callable
from .adapter.server_request_adapter import ServerRequestAdapter
from .adapter.config_audio_adapter import ConfigAudioAdapter
from .adapter.config_adapter import ConfigAdapter
from .adapter.socket_client import SocketAdapter
from typing import Dict, Any, Optional
from .config.config import CONFIG
from .dtos.output import (
    StatusOutputDTO,
    AvailableModelsOutputDTO,
    AvailableLLMsOutputDTO,
    AvailablePromptsOutputDTO,
    AudioTranscriptionOutputDTO,
)
from .dtos.input import StreamingInputDTO, MessageInputDTO
from .dtos.core_dto import EMessageType
from .enums.action_keys import ActionKeys
from .enums.language_keys import LanguageEnum
from .dtos.prompt_dto import PromptTemplate
from .dtos.core_dto import IMessage


class LLMStreamingClient:
    """Simplified client for the llm_streaming."""

    def __init__(
        self, base_url: Optional[str] = CONFIG.BASE_URL, timeout: int = CONFIG.TIMEOUT
    ) -> None:
        """
        Initialize the client.

        Args:
            base_url: Base URL of the service
            timeout: Maximum wait time for requests
        """
        self.base_url = base_url
        self.config_adapter = ConfigAdapter(timeout=timeout, base_url=self.base_url)
        self.config_audio_adapter = ConfigAudioAdapter(
            timeout=timeout, base_url=self.base_url
        )
        self.server_request_adapter = ServerRequestAdapter(
            timeout=timeout, base_url=self.base_url
        )
        self.socket_adapter = SocketAdapter(timeout=timeout, base_url=self.base_url)

    def get_status(self) -> StatusOutputDTO:
        """
        Get the status of the service.

        Returns:
            Dictionary with the status information.
        """
        return self.config_adapter.status()

    def get_models(self) -> AvailableModelsOutputDTO:
        """
        Get the list of available models.

        Returns:
            Dictionary with the available models.
        """
        return self.config_adapter.get_available_models()

    def get_llms(self) -> AvailableLLMsOutputDTO:
        """
        Get the list of available LLMs.

        Returns:
            Dictionary with the available LLMs.
        """
        return self.config_adapter.get_available_llms()

    def get_prompts(self) -> AvailablePromptsOutputDTO:
        """
        Get the list of available prompts with their metadata.

        Returns:
            List of dictionaries containing prompt metadata.
        """
        return self.config_adapter.get_available_prompts()

    def transcribe_audio(
        self, audio_service: str, audio_url: str
    ) -> AudioTranscriptionOutputDTO:
        """
        Transcribe an audio file using the specified audio service.

        Args:
            audio_service: The name of the audio service to use.
            audio_url: The audio file in binary format.

        Returns:
            A dictionary containing the transcription result.
        """
        return self.config_audio_adapter.transcribe_audio(audio_service, audio_url)

    def handle_request(
        self,
        text: str,
        action_key: ActionKeys,
        llm_name: str = "openai",
        model_name: str = "gpt-4o-mini",
        language: LanguageEnum = LanguageEnum.SPANISH,
        context_info: Optional[str] = None,
        image_object: Optional[Any] = None,
        session_id: Optional[str] = None,
    ) -> Dict[str, Any]:
        """
        Handle a request to the LLM service.

        Args:
            text: The input text for the request.
            action_key: The action key to determine the type of request.
            llm_name: The name of the LLM to use (default: "openai").
            model_name: The name of the model to use (default: "gpt-4o-mini").
            image_object: Optional image object for the request.
            session_id: Optional session ID for the request.

        Returns:
            A dictionary containing the response from the LLM service.
        """
        dto = MessageInputDTO(
            llm_name=llm_name,
            model_name=model_name,
            text=text or "",
            context_info=context_info,
            language=(
                LanguageEnum(language) if isinstance(language, str) else language
            ),
            action_key=(
                ActionKeys(action_key) if isinstance(action_key, str) else action_key
            ),
            image_object=image_object,
            session_id=session_id,
        )
        return self.server_request_adapter.handle_request(dto)

    def send_messages_via_socket(
        self,
        text: str,
        action_key: ActionKeys = "default",
        llm: Optional[str] = "google",
        model: Optional[str] = "gemini-2.5-flash-lite",
        language: Optional[LanguageEnum] = LanguageEnum.SPANISH,
        prompt: Optional[PromptTemplate] = None,
        image_object: Optional[Any] = None,
        session_id: Optional[str] = None,
        context_info: Optional[str] = None,
        on_token: Optional[Callable[[str, bool], None]] = None,
    ) -> None:
        """
        Send messages to the LLM service via Socket.IO and stream the response tokens.
        Args:
            text: The input text to send.
            action_key: The action key to determine the type of request (default: "default").
            llm: The name of the LLM to use (default: "openai").
            model: The name of the model to use (default: "gpt-4o-mini").
            language: The language of the input text (default: LanguageEnum.SPANISH).
            prompt: Optional prompt template to use.
            image_object: Optional image object for the request.
            session_id: Optional session ID for the request.
            context_info: Optional context information for the request.
            on_token: Optional callback function to handle each token received. It should accept two parameters:
                        the token content (str) and a boolean indicating if the stream is finished.
        Returns:
            None
        """

        dto = StreamingInputDTO(
            llm_name=llm,
            model_name=model,
            text=text,
            prompt=prompt,
            language=language,
            action_key=(
                ActionKeys(action_key) if isinstance(action_key, str) else action_key
            ),
            image_object=image_object,
            session_id=session_id,
            context_info=context_info,
        )
        self.socket_adapter.send_messages(dto, on_token=on_token)
