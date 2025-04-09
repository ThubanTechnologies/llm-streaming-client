from typing import Dict, Any, Optional
import requests
from io import BytesIO
from .exceptions import FileManagerAdapterException
from ..dtos.dto import FileResponse
from src.llm_streaming_client.config.config import CONFIG

class HttpClient:
    """HTTP client for making requests to the file manager service."""
    
    def __init__(self, timeout: int = CONFIG.TIMEOUT) -> None:
        self.timeout: int = timeout
        self.session = requests.Session()      

    def _make_request(self, method: str, url: str, **kwargs) -> Dict[str, Any]:
        """Make HTTP request expecting JSON response."""
        response: requests.Response = self._make_raw_request(method, url, **kwargs)
        return response.json()

    def _make_raw_request(self, method: str, url: str, **kwargs) -> requests.Response:
        """Make HTTP request and return raw response."""
        try:
            response: requests.Response = self.session.request(method, url, timeout=self.timeout, **kwargs)
            response.raise_for_status()
            return response
        except requests.exceptions.RequestException as e:
            error_msg: str = f"HTTP {method} request to {url} failed: {str(e)}"
            raise FileManagerAdapterException(error_msg) from e

    def _get(self, url: str, params: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """
        Performs a GET request and returns the JSON response.

        Args:
            url: The URL to send the GET request to.
            params: Optional query parameters.

        Returns:
            A dictionary containing the JSON response.
        """
        return self._make_request('GET', url, params=params)

    def _post(self, url: str, data: Optional[Dict[str, Any]] = None, files: Optional[Dict[str, Any]] = None, json: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """
        Performs a POST request and returns the JSON response.

        Args:
            url: The URL to send the POST request to.
            data: Optional form data to include in the request.
            files: Optional files to include in the request.

        Returns:
            A dictionary containing the JSON response.
        """
        return self._make_request('POST', url, data=data, files=files, json=json)