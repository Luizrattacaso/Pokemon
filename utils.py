import requests
from io import BytesIO
from PIL import Image, ImageTk

base_url = "https://pokeapi.co/api/v2/"

def get_pokemon_info(pokemon):
    url = f"{base_url}pokemon/{pokemon}"
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

def description(pokemon):
    url = f"{base_url}pokemon-species/{pokemon.lower()}/"
    try:
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            description = data["flavor_text_entries"][0]["flavor_text"]
            if description == None:
                return f"it's not possible to search\nfor information about {pokemon}"
            else:
                return description
        else:
            print(f"Something gone wrong. Status code: {response.status_code}")
    except ValueError as v:
        return f"Value Error: {v}"
    except Exception as e:
        return f"Error: {e}"

def load_image(name):
    try:
        url = f"https://play.pokemonshowdown.com/sprites/gen5/{name.lower()}.png"
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        img_data = BytesIO(response.content)
        img = Image.open(img_data)
        img = img.resize((220, 220), Image.Resampling.LANCZOS)
        return ImageTk.PhotoImage(img)
    except Exception as e:
        print(f"Erro ao carregar imagem online: {e}")
        return None
