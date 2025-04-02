from typing import Dict, Any, Optional
import requests
from io import BytesIO
from .exceptions import FileManagerAdapterException
from ..dtos.dto import FileResponse

class HttpClient:
    """HTTP client for making requests to the file manager service."""
    
    def __init__(self, timeout: int = 30):
        self.timeout: int = timeout
        self.session = requests.Session()

    def post_file(self, url: str, data: Dict[str, Any], files: Dict[str, Any]) -> Dict[str, Any]:
        """Perform POST request with file upload."""
        return self._make_request('POST', url, data=data, files=files)

    def get_file(self, url: str, params: Optional[Dict[str, str]] = None) -> FileResponse:
        """Perform GET request to retrieve file."""
        response: requests.Response = self._make_raw_request('GET', url, params=params)
        
        content_type: str = response.headers.get('Content-Type', '')
        
        if 'application/json' in content_type:
            return FileResponse(
                content=response.json(),
                is_file=False
            )
        
        return FileResponse(
            content=BytesIO(response.content),
            filename=self._get_filename_from_headers(response),
            content_type=content_type,
            content_length=int(response.headers.get('Content-Length', 0)),
            is_file=True
        )

    def update_file(self, url: str, data: Dict[str, Any], files: Dict[str, Any]) -> Dict[str, Any]:
        """Perform PUT request to update file."""
        return self._make_request('PUT', url, data=data, files=files)

    def delete_file(self, url: str, params: Optional[Dict[str, str]] = None) -> Dict[str, Any]:
        """Perform DELETE request to remove file."""
        return self._make_request('DELETE', url, params=params)

    def _make_raw_request(self, method: str, url: str, **kwargs) -> requests.Response:
        """Make HTTP request and return raw response."""
        try:
            response: requests.Response = self.session.request(method, url, timeout=self.timeout, **kwargs)
            response.raise_for_status()
            return response
        except requests.exceptions.RequestException as e:
            error_msg: str = f"HTTP {method} request to {url} failed: {str(e)}"
            raise FileManagerAdapterException(error_msg) from e

    def _get_filename_from_headers(self, response: requests.Response) -> Optional[str]:
        """Extract filename from Content-Disposition header."""
        cd = response.headers.get('Content-Disposition')
        if cd and 'filename=' in cd:
            return cd.split('filename=')[-1].strip('"')
        return None

    def _make_request(self, method: str, url: str, **kwargs) -> Dict[str, Any]:
        """Make HTTP request expecting JSON response."""
        response: requests.Response = self._make_raw_request(method, url, **kwargs)
        return response.json()