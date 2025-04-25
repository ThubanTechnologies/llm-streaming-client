import pytest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../..")))
from src.llm_streaming_client.adapter.config_adapter import ConfigAdapter

@pytest.mark.parametrize(
    "method_name, config_key, mock_response",
    [
        ("status", "status", {"status": "ok"}),
        ("get_available_models", "available_models", {"models": ["gpt-4", "gpt-3.5"]}),
        ("get_available_llms", "available_llms", {"llms": ["openai", "anthropic"]}),
        ("get_available_prompts", "available_prompts", [{"name": "summarize"}]),
    ]
)
def test_config_adapter_methods(monkeypatch, method_name, config_key, mock_response):
    adapter = ConfigAdapter(base_url="http://mock-base-url")
    called = {}

    def fake_get(url):
        called["url"] = url
        return mock_response

    monkeypatch.setattr(adapter, "_get", fake_get)

    method = getattr(adapter, method_name)
    result = method()

    assert result == mock_response
    expected_url = "http://mock-base-url" + adapter._config[config_key]
    assert called["url"] == expected_url
