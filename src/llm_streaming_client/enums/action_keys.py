from enum import Enum


class ActionKeys(Enum):
    """
    Enum for defining action keys used in the application.

    This enumeration provides a set of predefined keys that represent
    different actions within the application.

    Attributes:
        DEFAULT (str): The default action key.
        SUMMARIZE (str): The action key used for summarization operations.
    """

    DEFAULT = "default"
    SUMMARIZE = "summarize"
    IMAGE_EXTRACTION = "extract"
    IMAGE_DESCRIPTION = "describe"
