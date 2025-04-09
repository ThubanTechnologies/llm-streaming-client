from typing import Dict, Any, Optional
from .http_client import HttpClient
from src.llm_streaming_client.config.config import CONFIG

class ServerRequestAdapter(HttpClient):
    """Adapter to interact with the request handling microservice paths."""

    def __init__(self, base_url: str, timeout: int = CONFIG.TIMEOUT) -> None:
        super().__init__(timeout=timeout)
        self._config = CONFIG.server_request_adapter
        self.base_url = base_url

    def handle_request(
        self,
        text: Optional[str],
        action_key: str,
        llm_name: Optional[str] = None,
        model_name: Optional[str] = None,
        image_object: Optional[Any] = None,
    ) -> Dict[str, Any]:
        """
        Sends a request to the LLM service and retrieves the response.

        Args:
            text: The input text for the request.
            action_key: The action key to determine the type of request.
            llm_name: The name of the LLM to use (default: "openai").
            model_name: The name of the model to use (default: "gpt-4o-mini").
            image_object: Optional image object for the request.

        Returns:
            A dictionary containing the response from the LLM service.
        """
        data = {
            "text": text,
            "actionKey": action_key,
            "llm_name": llm_name,
            "model_name": model_name,
            "image": image_object,
        }

        url = self.base_url + self._config["request"]
        return self._post(url, json=data)