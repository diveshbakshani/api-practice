# basic practice
"""
Write code to retrieve data from an API and store it in a database. For example, you could be asked to retrieve data about movies from a movie API and store it in a PostgreSQL database. You would need to make an HTTP request to the API, parse the JSON response, and insert the data into the database. This would require knowledge of how to use Python libraries for working with databases, as well as how to parse JSON data and handle errors.
"""

import requests
import json
# import psycopg2
import os

# get API key from environment variable
API_KEY = os.environ.get('API_KEY')
API_KEY = "dc6295e410c585886b4d761857bfeb6a"

params = { "api_key": API_KEY }
url = "https://api.themoviedb.org/3/movie/"
movie_id = 550

response = requests.get(url + str(movie_id), params=params)
data = response.json()
# print(data)