import requests
from io import BytesIO

from check_id import check_id

base_url = "https://pokeapi.co/api/v2/"

def get_pokemon_info(pokemon):

    pokemon = check_id(pokemon)

    url = f"{base_url}pokemon/{pokemon.lower()}/"
    response = requests.get(url)

    try:
        if response.status_code == 200:
            information = response.json()
            print(information["sprites"]["front_default"])
            return information
        else:
            return print(f"Status code: {response.status_code}")

    except Exception as Error:
        return f"Error: {Error}"
