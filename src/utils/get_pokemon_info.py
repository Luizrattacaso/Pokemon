import requests

from src.utils.check_id import check_pokemon_id

base_url = "https://pokeapi.co/api/v2/"

def get_pokemon_info(pokemon):
    pokemon = check_pokemon_id(pokemon)

    url = f"{base_url}pokemon/{pokemon.lower()}/"
    response = requests.get(url, timeout=10)

    try:
        if response.status_code == 200:
            information = response.json()
            return information

        return f"Status code: {response.status_code}"

    except Exception as error:
        return f"Error: {error}"