# These DTOs have been extracted from the LLM_Streaming microservice to ensure consistency across projects.
from dataclasses import dataclass
from typing import List, Optional
from llm_streaming_client.dtos.core_dto import IMessage
from llm_streaming_client.enums.action_keys import ActionKeys
from llm_streaming_client.dtos.prompt_dto import PromptTemplate
from llm_streaming_client.enums.language_keys import LanguageEnum


@dataclass
class StreamingInputDTO:
    """
    DTO for inputs to streaming responses from LLMs.
    Contains all the data needed to process a streaming response request.
    """

    llm_name: str
    model_name: str
    messages: List[IMessage]
    prompt: PromptTemplate
    language: LanguageEnum
    action_key: ActionKeys
    image_object: Optional[str] = None


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
    image_object: Optional[str] = None
