class CONFIG:
    BASE_URL = "http://localhost:5000"
    API_VERSION = "/v1"
    API_PREFIX = "/api" + API_VERSION + "/chat"
    SOCKET_NAMESPACE = API_PREFIX

    TIMEOUT = 30
    RECONNECT_ATTEMPTS = 3
    config_adapter = {
        "status": f"{API_PREFIX}/status",
        "available_models": f"{API_PREFIX}/available_models",
        "available_llms": f"{API_PREFIX}/available_llms",
        "available_prompts": f"{API_PREFIX}/available_prompts",
    }
    config_audio_adapter = {
        "audio": f"{API_PREFIX}/audio",
    }
    server_request_adapter = {
        "request": f"{API_PREFIX}/request",
    }
