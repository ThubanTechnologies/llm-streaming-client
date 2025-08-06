from typing import Dict, Any, Optional
import requests
from ..config.config import CONFIG
from ..utils.http_client_utils import build_success_response, build_error_response


class HttpClient:
    """HTTP client for making requests to the llm-streaming service."""

    def __init__(self, timeout: int = CONFIG.TIMEOUT) -> None:
        self.timeout: int = timeout
        self.session = requests.Session()

    def _make_request(self, method: str, url: str, **kwargs) -> Dict[str, Any]:
        """Make HTTP request expecting JSON response."""
        try:
            response = self.session.request(method, url, timeout=self.timeout, **kwargs)
            response.raise_for_status()
            return build_success_response(response)
        except requests.exceptions.RequestException as e:
            return build_error_response(e)

    def _make_raw_request(self, method: str, url: str, **kwargs) -> requests.Response:
        """Make HTTP request and return raw response."""
        response = self.session.request(method, url, timeout=self.timeout, **kwargs)
        return response

    def _get(self, url: str, params: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """
        Performs a GET request and returns the JSON response.

        Args:
            url: The URL to send the GET request to.
            params: Optional query parameters.

        Returns:
            A dictionary containing the JSON response.
        """
        return self._make_request("GET", url, params=params)

    def _post(
        self,
        url: str,
        data: Optional[Dict[str, Any]] = None,
        files: Optional[Dict[str, Any]] = None,
        json: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        """
        Performs a POST request and returns the JSON response.

        Args:
            url: The URL to send the POST request to.
            data: Optional form data to include in the request.
            files: Optional files to include in the request.

        Returns:
            A dictionary containing the JSON response.
        """
        return self._make_request("POST", url, data=data, files=files, json=json)
