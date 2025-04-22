from dataclasses import dataclass
from typing import List
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

    def append_language(self, language: LanguageEnum) -> None:
        """
        Adds language information to the prompt content.
        """
        self.description += f"\n\n Output Language: {language.value}"
