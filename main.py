import requests
from tkinter import *
from tkinter import ttk
from random import Random

from src.program.frame_window import frame_window
from src.program.main_frame import main_frame
from src.utils.get_description import description
from src.utils.get_pokeball_image import pokeball_image
from src.utils.get_pokemon_info import get_pokemon_info
from src.utils.load_pokemon_image import load_image

co0 = "#09090C"
co1 = "#feffff"
co5 = "#ef5350"
co7 = "#a5e286"

window = Tk()
window.title("Pokemons")
window.geometry("550x510")
window.resizable(False, False)

try:
    icone = PhotoImage(file="icon/icone-pikachu.png")
    window.iconphoto(False, icone)
except Exception:
    pass

window.config(bg=co1)

ttk.Separator(window, orient=HORIZONTAL).grid(row=0, columnspan=1, ipadx=272)

style = ttk.Style(window)
style.theme_use("clam")

frame_pokemon = Frame(window, width=550, height=350, relief="flat", background=co7)
frame_pokemon.grid(row=1, column=0)

frame_type = main_frame(texto="type", frame_pokemon=frame_pokemon)
frame_name = main_frame(texto="your pokemon", fonte="Fixedsys 20 bold", frame_pokemon=frame_pokemon)
frame_id = main_frame(texto="#id", frame_pokemon=frame_pokemon)
description_frame = main_frame(
    texto="Here will be the description of the pokemon",
    anchor=NW,
    fonte="lvy 12",
    justify="left",
    wraplength=150,
    frame_pokemon=frame_pokemon,
)

frame_name.place(x=12, y=15)
frame_type.place(x=12, y=50)
frame_id.place(x=12, y=75)
description_frame.place(x=375, y=100)
description_frame.lift()

pokeball = pokeball_image()
frame_image = Label(frame_pokemon, image=pokeball, bg=co7)
frame_image.place(x=180, y=210)

frame_type.lift()

status_pokemon = frame_window(master=window, texto="Information")
pokemon_height = frame_window(master=window, texto="• Height: m", fonte="lvy 10")
pokemon_weight = frame_window(master=window, texto="• Weight: Kg", fonte="lvy 10")
moves_pokemon = frame_window(master=window, texto="Moves")

status_pokemon.place(x=15, y=360)
pokemon_height.place(x=15, y=400)
pokemon_weight.place(x=15, y=425)
moves_pokemon.place(x=285, y=360)

entry_pokemon = Entry(window, font=("verdana 12"), width=20, bg=co1, fg=co0, relief="solid")
entry_pokemon.place(x=300, y=10)

def new_pokemon():
    new_pokemon_name = entry_pokemon.get().strip().lower()

    if not new_pokemon_name:
        description_frame.config(text="Please enter a Pokémon name.")
        return

    if new_pokemon_name == "random":
        new_pokemon_name = str(Random().randint(1, 1025))

    color_types = {
        "normal": "#A8A77A", "fighting": "#C22E28", "flying": "#A9D4F0",
        "poison": "#B763CD", "ground": "#E2BF65", "rock": "#B6A136",
        "bug": "#A2D97C", "ghost": "#755793", "steel": "#C5CBA3",
        "fire": "#EE8130", "water": "#6390F0", "grass": "#7AC74C",
        "electric": "#E1C75F", "psychic": "#F95587", "ice": "#96D9D6",
        "dragon": "#7C5AD2", "dark": "#705746", "fairy": "#D685AD",
        "stellar": "#6A4C9C", "unknown": "#DFC570",
    }

    try:
        new_information = get_pokemon_info(new_pokemon_name)
        if not new_information:
            raise ValueError("Pokémon data not found")

        new_desc = description(new_pokemon_name)
        if not new_desc or new_desc.strip() == "":
            new_desc = "No description available."
        else:
            new_desc = new_desc.replace("\n", " ").replace("\f", " ")

        type_name = new_information["types"][0]["type"]["name"].lower()
        back_ground = color_types.get(type_name, "#CCCCCC")

        frame_pokemon.config(bg=back_ground)
        frame_name.config(text=new_information["name"].capitalize(), bg=back_ground)
        frame_type.config(text=type_name.capitalize(), bg=back_ground)
        frame_id.config(text=f"#{new_information['id']}", bg=back_ground)
        description_frame.config(text=new_desc, bg=back_ground)
        pokemon_height.config(text=f"• Height: {new_information['height']/10} m")
        pokemon_weight.config(text=f"• Weight: {new_information['weight']/10} Kg")

        new_image = load_image(new_pokemon_name)
        if new_image:
            frame_image.config(image=new_image, bg=back_ground)
            frame_image.image = new_image
            frame_image.place(x=100, y=80)
        else:
            frame_image.config(image=None, text="Image not available", font=("lvy 10"), fg="white", bg=back_ground)
            frame_image.place(x=100, y=80)

        for widget in window.winfo_children():
            if isinstance(widget, Label) and 290 <= widget.winfo_x() <= 450 and widget.winfo_y() >= 360:
                widget.destroy()

        new_moves = new_information["moves"][:3]
        for idx, movimento_info in enumerate(new_moves):
            move_name = movimento_info["move"]["name"].replace("-", " ").title()
            pokemon_move = frame_window(master=window, texto=f"• {move_name}", fonte="lvy 10", anchor="w")
            pokemon_move.place(x=290, y=400 + idx * 30)

    except requests.exceptions.ConnectionError:
        description_frame.config(text="❌ Connection error.\nCheck your internet connection.")
        frame_image.config(image=None, text="❌ No connection", font=("lvy 10"), fg="red", bg=co7)
        print("Erro: Sem conexão com a internet.")

    except requests.exceptions.Timeout:
        description_frame.config(text="⏳ Request timed out.\nTry again later.")
        print("Erro: Tempo de requisição excedido.")

    except requests.exceptions.RequestException as e:
        description_frame.config(text="⚠️ Request failed.\nCheck network or try again.")
        print(f"Erro de requisição: {e}")

    except KeyError:
        description_frame.config(text="⚠️ Invalid data format.\nPokémon may not exist.")
        print("Erro: Dados incompletos ou mal formatados.")

    except ValueError as e:
        if "not found" in str(e).lower():
            description_frame.config(text="❌ Pokémon not found.\nCheck the spelling.")
        else:
            description_frame.config(text="⚠️ Invalid input.")
        print(f"Erro: {e}")

    except Exception as e:
        description_frame.config(text="⚠️ An unexpected error occurred.")
        print(f"Erro inesperado: {e}")

entry_pokemon.bind("<Return>", lambda event: new_pokemon())

botao_buscar = Button(
    window,
    text="Search",
    command=new_pokemon,
    font=("verdana 10 bold"),
    bg=co5,
    fg=co1,
    relief="raised",
    overrelief=RIDGE,
)

botao_buscar.place(x=460, y=9)

if __name__ == "__main__":
    window.mainloop()