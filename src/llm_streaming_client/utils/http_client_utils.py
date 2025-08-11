from typing import Any, Dict
import requests


def build_success_response(response: requests.Response) -> Dict[str, Any]:
    """Build successful response structure."""
    json_response = response.json()
    return {
        "success": True,
        "response": json_response,
        "error": None,
    }


def build_error_response(
    exception: requests.exceptions.RequestException,
) -> Dict[str, Any]:
    """Build error response structure."""
    error_message = _extract_error_message(exception)
    return {"success": False, "response": None, "error": error_message}


def _extract_error_message(exception: requests.exceptions.RequestException) -> str:
    """Extract error message from request exception."""
    if not hasattr(exception, "response") or exception.response is None:
        return "Connection error: " + str(exception)

    try:
        response_json = exception.response.json()
        return _parse_api_error_message(response_json, exception.response.status_code)
    except Exception:
        return _get_response_parsing_error_message(exception.response)


def _parse_api_error_message(response_json: Dict[str, Any], status_code: int) -> str:
    """Parse error message from API response JSON."""
    if "error" in response_json and response_json["error"]:
        return _extract_from_error_field(response_json["error"], status_code)

    error_data = response_json.get("error_message", "Unknown error")
    return _extract_from_error_message_field(error_data, status_code)


def _extract_from_error_field(error_data: Any, status_code: int) -> str:
    """Extract error message from 'error' field."""
    if isinstance(error_data, dict) and "message" in error_data:
        return f"Code: {status_code}, Error: {error_data['message']}"
    else:
        return f"Code: {status_code}, Error: {error_data}"


def _extract_from_error_message_field(error_data: Any, status_code: int) -> str:
    """Extract error message from 'error_message' field."""
    if _is_formatted_error_string(error_data):
        return _parse_formatted_error_string(error_data)
    elif isinstance(error_data, dict) and "message" in error_data:
        return f"Code: {status_code}, Error: {error_data['message']}"
    else:
        return f"Code: {status_code}, Error: {error_data}"


def _is_formatted_error_string(error_data: Any) -> bool:
    """Check if error_data is a formatted error string."""
    return (
        isinstance(error_data, str)
        and "Error code:" in error_data
        and "{'error':" in error_data
    )


def _parse_formatted_error_string(error_string: str) -> str:
    """Parse formatted error string like 'Error code: X - {'error': {'message': 'Y'}}'."""
    try:
        code = error_string.split(" - ")[0].replace("Error code: ", "")
        dict_part = error_string.split(" - ", 1)[1]
        error_dict = eval(dict_part)
        message = error_dict["error"]["message"]
        return f"Code: {code}, Error: {message}"
    except Exception:
        return f"Error: {error_string}"


def _get_response_parsing_error_message(response: requests.Response) -> str:
    """Get error message when response JSON parsing fails."""
    response_text = getattr(response, "text", "No response text available")
    truncated_text = response_text[:200]
    if len(response_text) > 200:
        truncated_text += "..."
    return f"Code: {response.status_code}, Error: {truncated_text}"
