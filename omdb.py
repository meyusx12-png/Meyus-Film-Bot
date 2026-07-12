import os
import random
import requests

API_KEY = os.getenv("OMDB_API_KEY")

FILMS = [
    "Interstellar",
    "The Dark Knight",
    "Inception",
    "Fight Club",
    "The Prestige",
    "The Matrix",
    "Forrest Gump",
    "Whiplash",
    "Se7en",
    "Gladiator",
    "The Green Mile",
    "Parasite",
    "The Shawshank Redemption",
    "The Godfather",
    "Joker"
]

def get_random_movie():
    movie = random.choice(FILMS)

    url = f"https://www.omdbapi.com/?apikey={API_KEY}&t={movie}"

    data = requests.get(url).json()

    return data