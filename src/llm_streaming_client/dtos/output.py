# These DTOs have been extracted from the LLM_Streaming microservice to ensure consistency across projects.
from dataclasses import dataclass
from typing import Optional, List, Dict


@dataclass
class ResponseOutputDTO:
    """
    DTO for HTTP responses sent to clients.
    """

    response: Optional[str]
    status: str
    error_message: Optional[str] = None


@dataclass
class ErrorResponseDTO:
    """
    DTO for error responses sent to clients.
    """

    error: str


@dataclass
class SocketOutputDTO:
    """
    DTO for responses sent over socket connections.
    Contains the streaming response token and completion status.
    """

    content: str
    finished: bool


@dataclass
class SocketErrorDTO:
    """
    DTO for error messages sent over socket connections.
    """

    error_message: str


@dataclass
class StatusOutputDTO:
    """
    DTO for status endpoint response.
    """

    status: str


@dataclass
class AvailableModelsOutputDTO:
    """
    DTO for available models endpoint response.
    """

    models: Dict[str, List[str]]


@dataclass
class AvailableLLMsOutputDTO:
    """
    DTO for available LLMs endpoint response.
    """

    llms: List[str]


@dataclass
class PromptInfoDTO:
    """
    DTO for prompt information.
    """

    title: str
    actionKey: str


@dataclass
class AvailablePromptsOutputDTO:
    """
    DTO for available prompts endpoint response.
    """

    prompts: List[PromptInfoDTO]


@dataclass
class AudioTranscriptionOutputDTO:
    """
    DTO for audio transcription endpoint response.
    """

    text: str
