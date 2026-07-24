import requests
from io import BytesIO
from PIL import Image

try:
    from PIL import ImageTk
except ImportError:
    ImageTk = None

from src.utils.check_id import check_pokemon_id


def load_image(name):
    pokemon = check_pokemon_id(name)

    try:
        url = f"http://play.pokemonshowdown.com/sprites/home-centered/{pokemon.lower()}.png"
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        img_data = BytesIO(response.content)
        img = Image.open(img_data)
        img = img.resize((220, 220), Image.Resampling.LANCZOS)
        if ImageTk is None:
            return None
        return ImageTk.PhotoImage(img)
    except Exception as e:
        print(f"Erro ao carregar imagem online: {e}")
        return None