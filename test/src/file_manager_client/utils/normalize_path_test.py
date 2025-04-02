import pytest
from src.file_manager_client.utils.normalize_path import normalize_path

@pytest.mark.parametrize(
    "input_path, expected_output",
    [
        ("\\bucket\\folder\\subfolder", "bucket/folder/subfolder"),  
        ("/bucket/folder/subfolder", "bucket/folder/subfolder"),  
        ("bucket/folder/subfolder", "bucket/folder/subfolder"),    
        ("\\bucket/folder\\subfolder\\", "bucket/folder/subfolder/"),
        ("", ""),                                                 
        (None, None),                                            
    ]
)
def test_normalize_path(input_path, expected_output):
    assert normalize_path(input_path) == expected_output