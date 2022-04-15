"""File with app functions."""

import httpx

HOST_URL = "https://pokeapi.co/api/v2"


def get_pokemon_data(pokemon_name: str):
    """Make http request to get pokemon data."""
    METHOD = "pokemon"
    try:
        data = call_pokemon_api(METHOD, pokemon_name)
        return {"status_code": data.status_code, "data": data.json()}
    except httpx.HTTPStatusError as exc:
        print(f"Error response {exc.response.status_code} while requesting {exc.request.url!r}.")
        return {"status_code": exc.response.status_code,
                "error": f"Error response {exc.response.status_code} {exc.response.text!r}."}


def call_pokemon_api(method: str = None, detail: str = None):
    """Generic http request function."""
    headers = {
        'content-type': "application/json",
        'accept': "application/json"
    }

    data = httpx.get("/".join([HOST_URL, method, detail]), headers=headers)
    data.raise_for_status()
    return data
