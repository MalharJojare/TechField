import requests

from config import config


BASE_URL = "https://api.giphy.com/v1/gifs/search"


def search_giphy(query: str, limit: int = 10):
    query = query[:50]
    params = {
        "api_key": config.GIPHY_API_KEY,
        "q": query,
        "limit": limit,
        "rating": "pg"
    }

    response = requests.get(
        BASE_URL,
        params=params,
        timeout=10
    )

    response.raise_for_status()

    data = response.json()

    gifs = []

    for gif in data["data"]:

        gifs.append(
            {
                "title": gif["title"],
                "url": gif["images"]["original"]["url"],
                "id": gif["id"]
            }
        )

    return gifs