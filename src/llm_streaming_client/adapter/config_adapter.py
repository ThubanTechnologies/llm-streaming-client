from typing import Dict, Any, List
from .http_client import HttpClient
from src.llm_streaming_client.config.config import CONFIG

class ConfigAdapter(HttpClient):
    """Adapter to interact with the configuration microservice paths."""

    def __init__(self, base_url: str, timeout: int = CONFIG.TIMEOUT) -> None:
        super().__init__(timeout=timeout)
        self.base_url = base_url
        self._config = CONFIG.config_adapter

    def status(self) -> Dict[str, Any]:
        """Checks the status of the service."""
        url = self.base_url + self._config["status"]
        return self._get(url)

    def get_available_models(self) -> Dict[str, Any]:
        """Gets the list of available models."""
        url = self.base_url + self._config["available_models"]
        return self._get(url)

    def get_available_llms(self) -> Dict[str, Any]:
        """Gets the list of available LLMs."""
        url = self.base_url + self._config["available_llms"]
        return self._get(url)

    def get_available_prompts(self) -> List[Dict[str, Any]]:
        """Gets the list of available prompts with their metadata."""
        url = self.base_url + self._config["available_prompts"]
        return self._get(url)