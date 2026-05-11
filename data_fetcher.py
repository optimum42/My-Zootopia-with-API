import os
from dotenv import load_dotenv
import requests

load_dotenv()
API_KEY = os.getenv("API_KEY")
REQUEST_URL = 'https://api.api-ninjas.com/v1/animals?name='


def fetch_data(animal_name):
    """
    Fetches the animals data for the animal 'animal_name'
    Loads a JSON from API ninjas (https://api-ninjas.com/)

    Returns: a list of animals, each animal is a dictionary:
    {
    'name': ...,
    'taxonomy': {
      ...
    },
    'locations': [
      ...
    ],
    'characteristics': {
      ...
    }
    },
    """
    url = REQUEST_URL + animal_name
    headers = {'X-Api-Key': API_KEY}
    response = requests.get(url, headers)
    return response.json()

