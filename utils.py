import requests
from io import BytesIO
from PIL import Image, ImageTk

base_url = "https://pokeapi.co/api/v2/"

def get_pokemon_info(pokemon):
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

def description(pokemon):
    url = f"{base_url}pokemon-species/{pokemon.lower()}/"
    try:
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            english_entries = [
                entry["flavor_text"]
                for entry in data["flavor_text_entries"]
                if entry["language"]["name"] == "en"
            ]
            if english_entries:
                return english_entries[0]
        else:
            print(f"Something gone wrong. Status code: {response.status_code}")
    except:
        return None

def load_image(name):
    try:
        url = f"http://play.pokemonshowdown.com/sprites/home-centered/{name.lower()}.png"
        response = requests.get(url, timeout=5)
        response.raise_for_status() #se tiver erro na resposta ele pula para o except
        img_data = BytesIO(response.content)
        img = Image.open(img_data)
        img = img.resize((220, 220), Image.Resampling.LANCZOS)
        return ImageTk.PhotoImage(img)
    except Exception as e:
        print(f"Erro ao carregar imagem online: {e}")
        return None
    
def pokeball_image():
    try:
        url = "http://play.pokemonshowdown.com/sprites/itemicons/poke-ball.png"
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        img_data = BytesIO(response.content)
        img = Image.open(img_data)
        img = img.resize((60, 60), Image.Resampling.LANCZOS)
        return ImageTk.PhotoImage(img)
    except Exception as e:
        print(f"Error trying to load photo: {e}")
        return None