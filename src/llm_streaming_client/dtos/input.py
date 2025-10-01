# These DTOs have been extracted from the LLM_Streaming microservice to ensure consistency across projects.
from dataclasses import dataclass
from typing import List, Optional
from ..dtos.core_dto import IMessage
from ..enums.action_keys import ActionKeys
from ..dtos.prompt_dto import PromptTemplate
from ..enums.language_keys import LanguageEnum


@dataclass
class StreamingInputDTO:
    """
    DTO for inputs to streaming responses from LLMs.
    Contains all the data needed to process a streaming response request.
    """

    llm_name: str
    model_name: str
    text: str
    prompt: PromptTemplate
    language: LanguageEnum
    action_key: ActionKeys
    context_info: Optional[str] = None
    image_object: Optional[str] = None
    session_id: Optional[str] = None


@dataclass
class MessageInputDTO:
    """
    DTO for non-streaming request inputs from clients.
    Contains all the data needed to process a standard response request.
    """

    llm_name: str
    model_name: str
    text: str
    language: LanguageEnum
    action_key: ActionKeys
    context_info: Optional[str] = None
    image_object: Optional[str] = None
    session_id: Optional[str] = None
