# This enum has been extracted from the LLM_Streaming microservice project.
from enum import Enum
from typing import Dict, Optional


class LanguageEnum(Enum):
    """Enumeration of supported languages with standardized ISO codes."""

    ENGLISH = "english"
    SPANISH = "spanish"
    FRENCH = "french"
    GERMAN = "german"
    ITALIAN = "italian"
    PORTUGUESE = "portuguese"
    CHINESE = "chinese"
    JAPANESE = "japanese"
    KOREAN = "korean"
    RUSSIAN = "russian"
    DUTCH = "dutch"


LANGUAGE_MAPPING: Dict[str, LanguageEnum] = {
    "en": LanguageEnum.ENGLISH,
    "eng": LanguageEnum.ENGLISH,
    "english": LanguageEnum.ENGLISH,
    "ingles": LanguageEnum.ENGLISH,
    "inglés": LanguageEnum.ENGLISH,
    "es": LanguageEnum.SPANISH,
    "esp": LanguageEnum.SPANISH,
    "spanish": LanguageEnum.SPANISH,
    "español": LanguageEnum.SPANISH,
    "espanol": LanguageEnum.SPANISH,
    "fr": LanguageEnum.FRENCH,
    "fra": LanguageEnum.FRENCH,
    "french": LanguageEnum.FRENCH,
    "francés": LanguageEnum.FRENCH,
    "frances": LanguageEnum.FRENCH,
    "français": LanguageEnum.FRENCH,
    "francais": LanguageEnum.FRENCH,
    "de": LanguageEnum.GERMAN,
    "deu": LanguageEnum.GERMAN,
    "ger": LanguageEnum.GERMAN,
    "german": LanguageEnum.GERMAN,
    "alemán": LanguageEnum.GERMAN,
    "aleman": LanguageEnum.GERMAN,
    "deutsch": LanguageEnum.GERMAN,
    "it": LanguageEnum.ITALIAN,
    "ita": LanguageEnum.ITALIAN,
    "italian": LanguageEnum.ITALIAN,
    "italiano": LanguageEnum.ITALIAN,
    "pt": LanguageEnum.PORTUGUESE,
    "por": LanguageEnum.PORTUGUESE,
    "portuguese": LanguageEnum.PORTUGUESE,
    "portugués": LanguageEnum.PORTUGUESE,
    "portugues": LanguageEnum.PORTUGUESE,
    "português": LanguageEnum.PORTUGUESE,
    "zh": LanguageEnum.CHINESE,
    "chi": LanguageEnum.CHINESE,
    "zho": LanguageEnum.CHINESE,
    "chinese": LanguageEnum.CHINESE,
    "chino": LanguageEnum.CHINESE,
    "mandarin": LanguageEnum.CHINESE,
    "mandarín": LanguageEnum.CHINESE,
    "ja": LanguageEnum.JAPANESE,
    "jpn": LanguageEnum.JAPANESE,
    "japanese": LanguageEnum.JAPANESE,
    "japonés": LanguageEnum.JAPANESE,
    "japones": LanguageEnum.JAPANESE,
    "ko": LanguageEnum.KOREAN,
    "kor": LanguageEnum.KOREAN,
    "korean": LanguageEnum.KOREAN,
    "coreano": LanguageEnum.KOREAN,
    "ru": LanguageEnum.RUSSIAN,
    "rus": LanguageEnum.RUSSIAN,
    "russian": LanguageEnum.RUSSIAN,
    "ruso": LanguageEnum.RUSSIAN,
    "nl": LanguageEnum.DUTCH,
    "nld": LanguageEnum.DUTCH,
    "dut": LanguageEnum.DUTCH,
    "dutch": LanguageEnum.DUTCH,
    "holandés": LanguageEnum.DUTCH,
    "holandes": LanguageEnum.DUTCH,
}


def get_language_enum(language_input: str) -> Optional[LanguageEnum]:
    """
    Converts a language input string to a standardized LanguageEnum.
    """
    normalized_input = language_input.lower().strip() if language_input else ""
    return LANGUAGE_MAPPING.get(normalized_input)


def get_default_language() -> LanguageEnum:
    """
    Returns the default language for the system.
    """
    return LanguageEnum.SPANISH
