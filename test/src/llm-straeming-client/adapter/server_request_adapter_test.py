import pytest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../..")))

from src.llm_streaming_client.adapter.server_request_adapter import ServerRequestAdapter
from src.llm_streaming_client.dtos.input import MessageInputDTO
from src.llm_streaming_client.enums.action_keys import ActionKeys
from src.llm_streaming_client.enums.language_keys import LanguageEnum


def test_handle_request_sends_correct_payload(monkeypatch):
    adapter = ServerRequestAdapter(base_url="http://mock-base-url")
    dto = MessageInputDTO(
        llm_name="openai",
        model_name="gpt-4o-mini",
        text="Hola mundo",
        language=LanguageEnum.SPANISH,
        action_key=ActionKeys.DEFAULT,
        image_object={"img": "mock"}
    )

    expected_url = "http://mock-base-url" + adapter._config["request"]
    expected_payload = {
        "llm_name": "openai",
        "model_name": "gpt-4o-mini",
        "text": "Hola mundo",
        "language": "spanish",
        "actionKey": "default",
        "image": {"img": "mock"},
    }
    mock_response = {"result": "ok"}
    called = {}

    def fake_post(url, json):
        called["url"] = url
        called["json"] = json
        return mock_response

    monkeypatch.setattr(adapter, "_post", fake_post)

    result = adapter.handle_request(dto)

    assert result == mock_response
    assert called["url"] == expected_url
    assert called["json"] == expected_payload
