import requests
from io import BytesIO
from PIL import Image, ImageTk

from check_id import check_id

def load_image(name):

    pokemon = check_id(name)
    
    try:
        url = f"http://play.pokemonshowdown.com/sprites/home-centered/{pokemon.lower()}.png"
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        img_data = BytesIO(response.content)
        img = Image.open(img_data)
        img = img.resize((220, 220), Image.Resampling.LANCZOS)
        return ImageTk.PhotoImage(img)
    except Exception as e:
        print(f"Erro ao carregar imagem online: {e}")
        return None