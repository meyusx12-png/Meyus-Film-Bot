import os
import random
import requests

API_KEY = os.getenv("TMDB_API_KEY")

def get_random_movie():
    # Rastgele bir sayfa seç (popüler filmlerden)
    page = random.randint(1, 20)

    url = "https://api.themoviedb.org/3/discover/movie"
    params = {
        "api_key": API_KEY,
        "language": "tr-TR",
        "sort_by": "popularity.desc",
        "page": page,
        "vote_count.gte": 100,
    }

    response = requests.get(url, params=params)
    results = response.json().get("results", [])

    if not results:
        return {"Response": "False"}

    movie = random.choice(results)

    # Detay ve tür bilgisi için ikinci istek
    detail_url = f"https://api.themoviedb.org/3/movie/{movie['id']}"
    detail_params = {"api_key": API_KEY, "language": "tr-TR"}
    detail = requests.get(detail_url, params=detail_params).json()

    genres = ", ".join([g["name"] for g in detail.get("genres", [])]) or "Bilinmiyor"
    runtime = detail.get("runtime")
    runtime_str = f"{runtime} dk" if runtime else "Bilinmiyor"

    poster_path = movie.get("poster_path")
    poster_url = f"https://image.tmdb.org/t/p/w500{poster_path}" if poster_path else "N/A"

    return {
        "Response": "True",
        "Title": movie.get("title"),
        "imdbRating": str(round(movie.get("vote_average", 0), 1)),
        "Year": (movie.get("release_date") or "????")[:4],
        "Genre": genres,
        "Runtime": runtime_str,
        "Plot": movie.get("overview") or "Açıklama bulunamadı.",
        "Poster": poster_url,
    }