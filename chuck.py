"""Fetch a random Chuck Norris joke from api.chucknorris.io."""

""" Importing json module to parse the JSON response from the API."""
import json 
""" Importing urllib to handle HTTP requests and errors."""
import urllib.request 
import urllib.error 


def fetch_chuck_joke():
    """Fetch a random Chuck Norris joke from the API."""
    url = "https://api.chucknorris.io/jokes/random"
    
    try:
        # Creating an opener object to handle the HTTP request, which allows us to set custom headers if needed
        opener = urllib.request.build_opener()
        # Setting a User-Agent header to mimic a browser request, which can help avoid being blocked by the server
        opener.addheaders = [('User-Agent', 'Mozilla/5.0')]
        # with statement ensures the response is properly closed after reading
        # The response is read and decoded from bytes to a string, then parsed as JSON to extract the joke
        with opener.open(url) as response:
            # Reading the response data and decoding it from bytes to a UTF-8 string, then parsing it as JSON to extract the joke
            data = response.read().decode('utf-8')
            # Parsing the JSON data to extract the joke text, which is located in the 'value' field of the JSON response
            joke_data = json.loads(data)
            # Returning the joke text, or a default message if the 'value' field is not found in the JSON response
            return joke_data.get('value', 'No joke found.')
    # Handle potential errors such as network issues or JSON parsing errors
    except urllib.error.URLError as e:
        return f"Failed to fetch joke: {e.reason}"
    except json.JSONDecodeError:
        return "Failed to parse joke data."

# if here to allow the function to be imported without executing the code below
if __name__ == "__main__":
    joke = fetch_chuck_joke()
    print(joke)