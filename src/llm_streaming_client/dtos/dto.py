from dataclasses import dataclass
from typing import Optional, Any, Dict, Union
from io import BytesIO

@dataclass
class FileResponse:
    """Response model for file operations."""
    content: Union[Dict[str, Any], BytesIO]
    filename: Optional[str] = None
    content_type: Optional[str] = None
    content_length: Optional[int] = None
    is_file: bool = False
    
    def __str__(self) -> str:            
        return (
            f"FileResponse(\n"
            f"\tcontent={ str(self.content)},\n"
            f"\tfilename={self.filename},\n"
            f"\tcontent_type={self.content_type},\n"
            f"\tcontent_length={self.content_length},\n"
            f"\tis_file={self.is_file}\n"
            f")"
        )
