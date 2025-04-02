class FileManagerAdapterException(Exception):
    """Base class for exceptions in the File Manager Adapter."""
    pass

class FileNotFoundException(FileManagerAdapterException):
    """Exception raised when a file is not found."""
    def __init__(self, message="File not found."):
        self.message: str = message
        super().__init__(self.message)

class FileUploadException(FileManagerAdapterException):
    """Exception raised for errors during file upload."""
    def __init__(self, message="Error occurred while uploading the file."):
        self.message: str = message
        super().__init__(self.message)

class FileUpdateException(FileManagerAdapterException):
    """Exception raised for errors during file update."""
    def __init__(self, message="Error occurred while updating the file."):
        self.message: str = message
        super().__init__(self.message)

class FileDeletionException(FileManagerAdapterException):
    """Exception raised for errors during file deletion."""
    def __init__(self, message="Error occurred while deleting the file."):
        self.message: str = message
        super().__init__(self.message)