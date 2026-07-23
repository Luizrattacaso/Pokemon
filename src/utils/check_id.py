import requests

base_url = "https://pokeapi.co/api/v2/"

def check_id(pokemon):
    if str(pokemon).isnumeric():
        pokemon = int(pokemon)
        url = f"{base_url}pokemon/{pokemon}/"
        response = requests.get(url)
        if response.status_code == 200:
            information = response.json()
            pokemon = information["name"]
        return pokemon
    return pokemon