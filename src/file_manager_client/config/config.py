"""
Configuration settings for the file manager client.

This module sets up the base URLs and endpoints for interacting with the file manager API.
"""

import os

_DEFAULT_URL = os.getenv("FILE_MANAGER_URL", "http://file-manager:5003")
_API_URI = "/api"
_API_VERSION = "/v1"
BASE_URL = f"{_DEFAULT_URL}{_API_URI}{_API_VERSION}"
FILE_ENDPOINT = f"{BASE_URL}/file"
STRUCTURE_ENDPOINT = f"{BASE_URL}/structure"
