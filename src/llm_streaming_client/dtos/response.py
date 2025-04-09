from dataclasses import dataclass
from typing import List, Dict, Any

@dataclass(frozen=True)
class FileEntity:
    """Represents a file entity in the system."""
    name: str
    size: int
    content: bytes

    def to_dict(self) -> Dict[str, Any]:
        """Convert the entity to a dictionary representation."""
        return {
            "name": self.name,
            "size": self.size,
            "content": self.content.decode('utf-8')
        }

@dataclass(frozen=True)
class FileListResponse:
    """Response containing a list of file entities."""
    files: List[FileEntity]

    def to_dict(self) -> Dict[str, List[Dict[str, Any]]]:
        """Convert the response to a dictionary representation."""
        return {
            "files": [file.to_dict() for file in self.files]
        }

@dataclass(frozen=True)
class ErrorResponse:
    """Response containing error information."""
    message: str
    code: str

    def to_dict(self) -> Dict[str, str]:
        """Convert the error to a dictionary representation."""
        return {
            "error": self.message,
            "code": self.code
        }