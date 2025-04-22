from dataclasses import dataclass
import datetime
from enum import Enum
from typing import List, Optional

from src.llm_streaming_client.dtos.prompt_dto import PromptTemplate
from src.llm_streaming_client.enums.language_keys import LanguageEnum
from src.llm_streaming_client.enums.action_keys import ActionKeys


class EMessageType(Enum):
    AI = "ai"
    USER = "user"
    ERROR = "error"


@dataclass
class IMessage:
    id: str
    content: str
    type: EMessageType
    timestamp: datetime


@dataclass
class StreamingDTO:
    """
    DTO for streaming responses from LLMs.
    """

    llm_name: str
    model_name: str
    messages: List[IMessage]
    prompt: PromptTemplate
    language: LanguageEnum
    action_key: ActionKeys
    image_object: Optional[str] = None

    def __str__(self) -> str:
        """
        Returns a string representation of the StreamingDTO.
        """

        image_display = (
            f", image_object={self.image_object}" if self.image_object else ""
        )
        return (
            f"StreamingDTO(\n"
            f"  llm_name={self.llm_name},\n"
            f"  model_name={self.model_name},\n"
            f"  messages={self.messages},\n"
            f"  prompt={self.prompt},\n"
            f"  language={self.language.value},\n"
            f"  action_key={self.action_key}{image_display}\n"
            f")"
        )


@dataclass
class MessageDTO:
    """
    DTO for messages in the request.
    Contains the message content and type.
    """

    llm_name: str
    model_name: str
    text: str
    prompt: PromptTemplate
    language: LanguageEnum
    action_key: ActionKeys
    image_object: Optional[str] = None

    def __str__(self) -> str:
        """
        Returns a string representation of the MessageDTO.
        """
        image_display = (
            f", image_object={self.image_object}" if self.image_object else ""
        )
        return (
            f"MessageDTO(\n"
            f"  llm_name={self.llm_name},\n"
            f"  model_name={self.model_name},\n"
            f"  text={self.text},\n"
            f"  prompt={self.prompt},\n"
            f"  language={self.language.value},\n"
            f"  action_key={self.action_key}{image_display}\n"
            f")"
        )
