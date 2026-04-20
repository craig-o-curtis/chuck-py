import json
from unittest.mock import MagicMock, patch

from chuck import fetch_chuck_joke


class TestFetchChuckJoke:
    """Tests for fetch_chuck_joke function."""

    def test_fetch_joke_success(self) -> None:
        """Successful API response returns joke."""
        mock_response = MagicMock()
        mock_response.read.return_value = json.dumps(
            {"value": "Chuck Norris can divide by zero."}
        ).encode()

        with patch("chuck.urllib.request.build_opener") as mock_opener:
            mock_opener.return_value.open.return_value.__enter__ = MagicMock(
                return_value=mock_response
            )
            mock_opener.return_value.open.return_value.__exit__ = MagicMock(
                return_value=False
            )

            result = fetch_chuck_joke()

        assert result == "Chuck Norris can divide by zero."

    def test_fetch_joke_no_value_field(self) -> None:
        """Missing 'value' field returns default message."""
        mock_response = MagicMock()
        mock_response.read.return_value = json.dumps({"other": "data"}).encode()

        with patch("chuck.urllib.request.build_opener") as mock_opener:
            mock_opener.return_value.open.return_value.__enter__ = MagicMock(
                return_value=mock_response
            )
            mock_opener.return_value.open.return_value.__exit__ = MagicMock(
                return_value=False
            )

            result = fetch_chuck_joke()

        assert result == "No joke found."

    def test_fetch_joke_network_error(self) -> None:
        """Network error returns error message."""
        from urllib.error import URLError

        with patch("chuck.urllib.request.build_opener") as mock_opener:
            mock_opener.return_value.open.side_effect = URLError("Connection refused")

            result = fetch_chuck_joke()

        assert result == "Failed to fetch joke: Connection refused"

    def test_fetch_joke_json_error(self) -> None:
        """Invalid JSON returns error message."""
        mock_response = MagicMock()
        mock_response.read.return_value = b"not valid json"

        with patch("chuck.urllib.request.build_opener") as mock_opener:
            mock_opener.return_value.open.return_value.__enter__ = MagicMock(
                return_value=mock_response
            )
            mock_opener.return_value.open.return_value.__exit__ = MagicMock(
                return_value=False
            )

            result = fetch_chuck_joke()

        assert result == "Failed to parse joke data."
