import requests
from io import BytesIO
from PIL import Image

try:
    from PIL import ImageTk
except ImportError:
    ImageTk = None


def pokeball_image():
    try:
        url = "http://play.pokemonshowdown.com/sprites/itemicons/poke-ball.png"
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        img_data = BytesIO(response.content)
        img = Image.open(img_data)
        img = img.resize((60, 60), Image.Resampling.LANCZOS)
        if ImageTk is None:
            return None
        return ImageTk.PhotoImage(img)
    except Exception as e:
        print(f"Error trying to load photo: {e}")
        return None