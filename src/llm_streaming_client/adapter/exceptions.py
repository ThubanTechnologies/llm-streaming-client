class LLMStreamingException(Exception):
    """Base exception for LLM Streaming errors."""
    default_message = "An unexpected error occurred"

    def __init__(self, message: str = None, error: Exception = None):
        self.original_error = error
        self.message = message or self.default_message

        final_message = f"{self.message}: {str(error)}" if error else self.message

        super().__init__(final_message)

class AudioTranscriptionException(LLMStreamingException):
    default_message = "Failed to transcribe audio"

class RequestHandlingException(LLMStreamingException):
    default_message = "Failed to handle request to LLM service"

class SocketCommunicationException(LLMStreamingException):
    default_message = "Socket communication error"
