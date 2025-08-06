from typing import Dict, Any, Optional
from .http_client import HttpClient
from ..config.config import CONFIG
from ..dtos.input import MessageInputDTO
from ..adapter.exceptions import RequestHandlingException


class ServerRequestAdapter(HttpClient):
    """Adapter to interact with the request handling microservice paths."""

    def __init__(self, base_url: str, timeout: int = CONFIG.TIMEOUT) -> None:
        super().__init__(timeout=timeout)
        self._config = CONFIG.server_request_adapter
        self.base_url = base_url

    def handle_request(self, dto: MessageInputDTO) -> Dict[str, Any]:
        """
        Sends a request to the LLM service and retrieves the response.

        Args:
            text: The input text for the request.
            action_key: The action key to determine the type of request.
            llm_name: The name of the LLM to use (default: "openai").
            model_name: The name of the model to use (default: "gpt-4o-mini").
            image_object: Optional image object for the request.
            session_id: Optional session ID for the request.

        Returns:
            A dictionary containing the response from the LLM service.
        """
        try:
            data = {
                "llm_name": dto.llm_name,
                "model_name": dto.model_name,
                "text": dto.text,
                "language": dto.language.value,
                "actionKey": dto.action_key.value,
            }
            if dto.image_object:
                data["image"] = dto.image_object
            if dto.session_id:
                data["session_id"] = dto.session_id
            if dto.context_info:
                data["context_info"] = dto.context_info

            url = self.base_url + self._config["request"]
            return self._post(url, json=data)
        except Exception:
            return {}
