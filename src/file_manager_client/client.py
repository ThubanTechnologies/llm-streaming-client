from typing import BinaryIO, Union, List, Dict, Any
from .adapter.file_adapter import FileAdapter
from .adapter.http_client import HttpClient
from .dtos.request import POSTFile, GETFile, PUTFile, DELETEFile, GETStructure
from .dtos.response import FileEntity
from .utils.normalize_path import normalize_path

class FileManagerClient:
    """Simplified client for the file manager."""

    def __init__(self, base_url: str, timeout: int = 30):
        """
        Initialize the client.
        
        Args:
            base_url: Base URL of the service
            timeout: Maximum wait time for requests
        """
        http_client = HttpClient(timeout=timeout)
        self.adapter = FileAdapter(base_url, http_client)

    def upload_file(self, bucket_id: str, directory: str, file: Union[str, BinaryIO]) -> FileEntity:
        """
        Upload a file to the service.
        
        Args:
            bucket_id: Bucket ID
            directory: Target directory
            file: File to upload (can be path or file object)
        """
        directory = normalize_path(directory)
        if isinstance(file, str):
            with open(file, 'rb') as f:
                request = POSTFile(bucket_id=bucket_id, directory=directory, file=f)
                return self.adapter.save_file(request)
        else:
            request = POSTFile(bucket_id=bucket_id, directory=directory, file=file)
            return self.adapter.save_file(request)

    def get_file(self, bucket_id: str, file_path: str) -> FileEntity:
        """
        Get a file from the service.
        
        Args:
            bucket_id: Bucket ID
            file_path: File path
        """
        file_path = normalize_path(file_path)
        request = GETFile(bucket_id=bucket_id, file_path=file_path)
        return self.adapter.get_file(request)
    
    def list_files(self, bucket_id: str, extensions: List[str] = None) -> Dict[str, Any]:
        """
        Get the file structure from the service.
        
        Args:
            bucket_id: Bucket ID
            extensions: Optional list of file extensions to filter by
        
        Returns:
            Dictionary with the file structure
        """
        request = GETStructure(bucket_id=bucket_id, extensions=extensions or [])
        return self.adapter.get_files(request)
    
    def update_file(self, bucket_id: str, directory: str, file: Union[str, BinaryIO]) -> FileEntity:
        """
        Update a file in the service.
        
        Args:
            bucket_id: Bucket ID
            directory: Target directory
            file: File to update (can be path or file object)
        """
        directory = normalize_path(directory)
        if isinstance(file, str):
            with open(file, 'rb') as f:
                request = PUTFile(bucket_id=bucket_id, directory=directory, file=f)
                return self.adapter.update_file(request)
        else:
            request = PUTFile(bucket_id=bucket_id, directory=directory, file=file)
            return self.adapter.update_file(request)

    def delete_file(self, bucket_id: str, file_path: str) -> bool:
        """
        Delete a file from the service.
        
        Args:
            bucket_id: Bucket ID
            file_path: File path
        """
        file_path = normalize_path(file_path)
        request = DELETEFile(bucket_id=bucket_id, file_path=file_path)
        return self.adapter.delete_file(request)
