# This enum has been extracted from the LLM_Streaming microservice.
from enum import Enum


class ActionKeys(Enum):
    """
    Enum for defining action keys used in the application.

    This enumeration provides a set of predefined keys that represent
    different actions within the application.

    Attributes:
        DEFAULT : The default action key. Used for answering questions based on provided document information, functioning as a chatbot.
        SUMMARIZE : Used to summarize documents.
        IMAGE_EXTRACTION : Used to extract text and tables from an image and return them in JSON format.
        IMAGE_DESCRIPTION : Used to generate a descriptive text for an image.
        SPARQL_QUERY : Used to execute a SPARQL query.
    """

    DEFAULT = "default"
    SUMMARIZE = "summarize"
    IMAGE_EXTRACTION = "extract"
    IMAGE_DESCRIPTION = "describe"
    SPARQL_QUERY = "sparql_query"
    
