"""Fetch a random Chuck Norris joke from api.chucknorris.io."""

import json
import urllib.request
import urllib.error


def fetch_chuck_joke():
    """Fetch a random Chuck Norris joke from the API."""
    url = "https://api.chucknorris.io/jokes/random"
    
    try:
        opener = urllib.request.build_opener()
        opener.addheaders = [('User-Agent', 'Mozilla/5.0')]
        with opener.open(url) as response:
            data = response.read().decode('utf-8')
            joke_data = json.loads(data)
            return joke_data.get('value', 'No joke found.')
    except urllib.error.URLError as e:
        return f"Failed to fetch joke: {e.reason}"
    except json.JSONDecodeError:
        return "Failed to parse joke data."


if __name__ == "__main__":
    joke = fetch_chuck_joke()
    print(joke)