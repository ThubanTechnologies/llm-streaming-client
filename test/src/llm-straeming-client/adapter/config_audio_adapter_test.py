import pytest

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../..")))
from src.llm_streaming_client.adapter.config_audio_adapter import ConfigAudioAdapter
from unittest.mock import mock_open, patch


def test_transcribe_audio_calls_post(monkeypatch):
    adapter = ConfigAudioAdapter(base_url="http://mock-base-url")
    audio_service = "whisper"
    audio_url = "fake_audio.wav"
    expected_url = "http://mock-base-url" + adapter._config["audio"]
    mock_response = {"transcription": "Hello world"}

    called = {}

    def fake_post(url, files=None, data=None):
        called["url"] = url
        called["files"] = files
        called["data"] = data
        return mock_response

    monkeypatch.setattr(adapter, "_post", fake_post)

    with patch("builtins.open", mock_open(read_data=b"fake-bytes")) as mock_file:
        result = adapter.transcribe_audio(audio_service, audio_url)

    assert result == mock_response
    assert called["url"] == expected_url
    assert "audio" in called["files"]
    assert called["files"]["audio"][0] == audio_url
    assert called["data"] == {"audio_service": audio_service}
