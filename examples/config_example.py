import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.llm_streaming_client.client import LLMStreamingClient
from src.llm_streaming_client.config.config import CONFIG

def main():
    base_url = CONFIG.BASE_URL
    timeout = CONFIG.TIMEOUT

    client = LLMStreamingClient(base_url, timeout)

    try:
        status = client.get_status()
        print("Service Status:", status)
    except Exception as e:
        print("Error getting status:", e)

    try:
        models = client.get_models()
        print("Available Models:", models)
    except Exception as e:
        print("Error getting models:", e)

    try:
        llms = client.get_llms()
        print("Available LLMs:", llms)
    except Exception as e:
        print("Error getting LLMs:", e)

    try:
        prompts = client.get_prompts()
        print("Available Prompts:", prompts)
    except Exception as e:
        print("Error getting prompts:", e)

if __name__ == "__main__":
    main()