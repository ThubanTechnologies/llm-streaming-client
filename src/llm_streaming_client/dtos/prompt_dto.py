# These DTOs have been extracted from the LLM_Streaming microservice to ensure consistency across projects.
from dataclasses import dataclass
from src.llm_streaming_client.enums.language_keys import LanguageEnum

@dataclass
class PromptTemplate:
    """
    Data class representing a prompt template with title and content.
    """

    title: str
    description: str
    temperature: float = 0.7

    def __str__(self) -> str:
        return (
            f"PromptTemplate(\n"
            f"\ttitle={self.title},\n"
            f"\tdescription={self.description},\n"
            f"\ttemperature={self.temperature}\n"
            f")"
        )