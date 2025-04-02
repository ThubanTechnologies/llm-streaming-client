from dataclasses import dataclass
from typing import Union, BinaryIO, TextIO, List

FileType = Union[BinaryIO, TextIO, str]

@dataclass
class FileRequest:
    """Base class for file-related requests."""
    bucket_id: str

@dataclass
class POSTFile(FileRequest):
    """Request model for file upload operation."""
    directory: str
    file: FileType

@dataclass
class GETFile(FileRequest):
    """Request model for file retrieval operation."""
    file_path: str

@dataclass
class GETStructure(FileRequest):
    """Request model for structure retrieval operation."""
    bucket_id: str
    extensions: List[str]

@dataclass
class PUTFile(FileRequest):
    """Request model for file update operation."""
    directory: str
    file: FileType

@dataclass
class DELETEFile(FileRequest):
    """Request model for file deletion operation."""
    file_path: str