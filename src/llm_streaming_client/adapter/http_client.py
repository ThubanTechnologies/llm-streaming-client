from typing import Dict, Any, Optional
import requests
import json
from ..config.config import CONFIG


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
            return self._build_success_response(response)
        except requests.exceptions.RequestException as e:
            return self._build_error_response(e)

    def _build_success_response(self, response: requests.Response) -> Dict[str, Any]:
        """Build successful response structure."""
        json_response = response.json()
        return {
            "success": True,
            "response": json_response.get("response"),
            "error": None,
        }

    def _build_error_response(
        self, exception: requests.exceptions.RequestException
    ) -> Dict[str, Any]:
        """Build error response structure."""
        error_message = self._extract_error_message(exception)
        return {"success": False, "response": None, "error": error_message}

    def _extract_error_message(
        self, exception: requests.exceptions.RequestException
    ) -> str:
        """Extract error message from request exception."""
        if not hasattr(exception, "response") or exception.response is None:
            return "Connection error: " + str(exception)

        try:
            response_json = exception.response.json()
            return self._parse_api_error_message(
                response_json, exception.response.status_code
            )
        except Exception:
            return self._get_response_parsing_error_message(exception.response)

    def _parse_api_error_message(
        self, response_json: Dict[str, Any], status_code: int
    ) -> str:
        """Parse error message from API response JSON."""
        if "error" in response_json and response_json["error"]:
            return self._extract_from_error_field(response_json["error"], status_code)

        error_data = response_json.get("error_message", "Unknown error")
        return self._extract_from_error_message_field(error_data, status_code)

    def _extract_from_error_field(self, error_data: Any, status_code: int) -> str:
        """Extract error message from 'error' field."""
        if isinstance(error_data, dict) and "message" in error_data:
            return f"Code: {status_code}, Error: {error_data['message']}"
        else:
            return f"Code: {status_code}, Error: {error_data}"

    def _extract_from_error_message_field(
        self, error_data: Any, status_code: int
    ) -> str:
        """Extract error message from 'error_message' field."""
        if self._is_formatted_error_string(error_data):
            return self._parse_formatted_error_string(error_data)
        elif isinstance(error_data, dict) and "message" in error_data:
            return f"Code: {status_code}, Error: {error_data['message']}"
        else:
            return f"Code: {status_code}, Error: {error_data}"

    def _is_formatted_error_string(self, error_data: Any) -> bool:
        """Check if error_data is a formatted error string."""
        return (
            isinstance(error_data, str)
            and "Error code:" in error_data
            and "{'error':" in error_data
        )

    def _parse_formatted_error_string(self, error_string: str) -> str:
        """Parse formatted error string like 'Error code: X - {'error': {'message': 'Y'}}'."""
        try:
            code = error_string.split(" - ")[0].replace("Error code: ", "")
            dict_part = error_string.split(" - ", 1)[1]
            error_dict = eval(dict_part)
            message = error_dict["error"]["message"]
            return f"Code: {code}, Error: {message}"
        except Exception:
            return f"Error: {error_string}"

    def _get_response_parsing_error_message(self, response: requests.Response) -> str:
        """Get error message when response JSON parsing fails."""
        response_text = getattr(response, "text", "No response text available")
        truncated_text = response_text[:200]
        if len(response_text) > 200:
            truncated_text += "..."
        return f"Code: {response.status_code}, Error: {truncated_text}"

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
