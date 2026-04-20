"""Fetch a random Chuck Norris joke from api.chucknorris.io."""

from __future__ import annotations

import json
import urllib.error
import urllib.request


def fetch_chuck_joke() -> str:
    """Fetch a random Chuck Norris joke from the API."""
    url = "https://api.chucknorris.io/jokes/random"

    try:
        opener = urllib.request.build_opener()
        opener.addheaders = [("User-Agent", "Mozilla/5.0")]
        with opener.open(url) as response:
            data = response.read().decode("utf-8")
            joke_data: dict[str, object] = json.loads(data)
            value = joke_data.get("value")
            if value is None:
                return "No joke found."
            return str(value)
    except urllib.error.URLError as e:
        return f"Failed to fetch joke: {e.reason}"
    except json.JSONDecodeError:
        return "Failed to parse joke data."


if __name__ == "__main__":
    while True:
        joke = fetch_chuck_joke()
        print(joke)
        answer = input("\nWould you like to hear another joke? [Y/n]: ").strip().lower()
        if answer in ("n", "no"):
            break
