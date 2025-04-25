import pytest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../..")))
from src.llm_streaming_client.adapter.socket_client import SocketAdapter
from src.llm_streaming_client.dtos.input import StreamingInputDTO
from src.llm_streaming_client.dtos.core_dto import IMessage, EMessageType
from src.llm_streaming_client.enums.action_keys import ActionKeys
from src.llm_streaming_client.enums.language_keys import LanguageEnum
from unittest.mock import MagicMock, patch


def test_send_messages_emits_correct_payload():
    adapter = SocketAdapter(base_url="http://mock-base-url")

    dto = StreamingInputDTO(
        llm_name="openai",
        model_name="gpt-4o-mini",
        messages=[
            IMessage(
                id="1",
                content="Hola",
                type=EMessageType.USER,
                timestamp="2024-01-01T12:00:00Z"
            )
        ],
        prompt=None,
        language=LanguageEnum.SPANISH,
        action_key=ActionKeys.DEFAULT,
        image_object=None,
    )

    with patch.object(adapter, "sio") as mock_sio:
        mock_sio.connected = True
        adapter.send_messages(dto)

        expected_payload = {
            "messages": [
                {
                    "id": "1",
                    "content": "Hola",
                    "type": "user",
                    "timestamp": "2024-01-01T12:00:00Z",
                }
            ],
            "llm_name": "openai",
            "model_name": "gpt-4o-mini",
            "actionKey": "default",
            "language": "spanish",
        }

        mock_sio.connect.assert_called_once_with("http://mock-base-url", namespaces=[adapter.namespace])
        mock_sio.emit.assert_called_once_with("send_message", expected_payload, namespace=adapter.namespace)
        mock_sio.wait.assert_called_once()
        mock_sio.disconnect.assert_called()
