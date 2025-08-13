from tkinter import *
from tkinter import ttk

from PIL import Image, ImageTk
from io import BytesIO
import requests

from utils import get_pokemon_info, description, load_image, pokeball_image

co0 = "#09090C"
co1 = "#feffff"
co5 = "#ef5350"
co7 = "#a5e286"

window = Tk()
window.title("Pokemons")
window.geometry("550x510")
window.resizable(False, False)

try:
    icone = PhotoImage(file="icon/cabeca-pikachu.png")
    window.iconphoto(False,icone)
except:
    pass

window.config(bg=co1)

ttk.Separator(window, orient= HORIZONTAL).grid(row=0,columnspan=1, ipadx=272)

style = ttk.Style(window)
style.theme_use("clam")

frame_pokemon = Frame(window, width= 550, height = 350, relief="flat", background=co7)
frame_pokemon.grid(row=1,column=0)

frame_nome = Label(frame_pokemon,
    text="your pokemon".capitalize(),
    relief="flat",
    anchor=CENTER,
    font=("Fixedsys 20 bold"),
    bg=co7,
    fg=co0)
frame_nome.place(x=12, y=15)

frame_tipo = Label(frame_pokemon,
    text=f"type".capitalize(),
    relief="flat",
    anchor=CENTER,
    font=("lvy 10 bold"),
    bg=co7,
    fg=co0)
frame_tipo.place(x=12, y=50)

frame_id = Label(frame_pokemon,
    text=f"#id".capitalize(),
    relief="flat",
    anchor=CENTER,
    font=("lvy 10 bold"),
    bg=co7,
    fg=co0)
frame_id.place(x=12, y=75)

description_frame = Label(frame_pokemon,
    text=f"Here will be the description of the pokemon",
    anchor=NW,
    font=("lvy 12"),
    bg=co7,
    fg=co0,
    justify="left",
    wraplength=150)  #break line
description_frame.place(x=375, y=100)

description_frame.lift()

#initial pokemon
pokeball = pokeball_image()

frame_imagem = Label(frame_pokemon, image=pokeball, bg=co7, fg=co7)
frame_imagem.place(x=180, y=210)

frame_tipo.lift() #o método lift sobrepõe

#status
status_pokemon = Label(window,
    text="Informations",
    relief="flat",
    anchor=CENTER,
    font=("verdana 20 bold"),
    bg=co1,
    fg=co0)
status_pokemon.place(x=15, y=360)

pokemon_height = Label(window, text=f"• Height: m", relief="flat", anchor=CENTER, font=("lvy 10"),bg=co1,fg=co0)
pokemon_height.place(x=15, y=400)

pokemon_weight = Label(window,
    text=f"• Weight: Kg",
    relief="flat",
    anchor=CENTER,
    font=("lvy 10"),
    bg=co1,
    fg=co0)
pokemon_weight.place(x=15, y=425)

#moves
moves_pokemon = Label(window,
    text="Moves",
    relief="flat",
    anchor=CENTER,
    font=("verdana 20 bold"),
    bg=co1,
    fg=co0)
moves_pokemon.place(x=285, y=360)

def new_pokemon():
    new_pokemon_name = entry_pokemon.get().strip().lower()
    if not new_pokemon_name:
        description_frame.config(text="Please enter a Pokémon name.")
        return
    
    color_types = {
        "normal": "#A8A77A", "fighting": "#C22E28", "flying": "#A9D4F0",
        "poison": "#B763CD", "ground": "#E2BF65", "rock": "#B6A136",
        "bug": "#A2D97C", "ghost": "#755793", "steel": "#C5CBA3",
        "fire": "#EE8130", "water": "#6390F0", "grass": "#7AC74C",
        "electric": "#ECCE58", "psychic": "#F95587", "ice": "#96D9D6",
        "dragon": "#7C5AD2", "dark": "#705746", "fairy": "#D685AD",
        "stellar": "#6A4C9C", "unknown": "#DFC570"
    }

    try:
        #try to get pokemon information
        new_information = get_pokemon_info(new_pokemon_name)
        if not new_information:
            raise ValueError("Pokémon data not found")

        # get descryption
        new_desc = description(new_pokemon_name)
        if not new_desc or new_desc.strip() == "":
            new_desc = "No description available."
        else:
            new_desc = new_desc.replace('\n', ' ').replace('\f', ' ')

        # type and background
        type_name = new_information["types"][0]["type"]["name"].lower()
        back_ground = color_types.get(type_name, "#CCCCCC")  # cor padrão se tipo desconhecido

        # Atualizar interface
        frame_pokemon.config(bg=back_ground)
        frame_nome.config(text=new_information["name"].capitalize(), bg=back_ground)
        frame_tipo.config(text=type_name.capitalize(), bg=back_ground)
        frame_id.config(text=f"#{new_information['id']}", bg=back_ground)
        description_frame.config(text=new_desc, bg=back_ground)
        pokemon_height.config(text=f"• Height: {new_information['height']/10} m")
        pokemon_weight.config(text=f"• Weight: {new_information['weight']/10} Kg")

        # load image
        new_image = load_image(new_pokemon_name)
        if new_image:
            frame_imagem.config(image=new_image, bg=back_ground)
            frame_imagem.image = new_image  # manter referência
            frame_imagem.place(x=100, y=80)
        else:
            frame_imagem.config(image=None, text="Image not available", font=("lvy 10"), fg="white", bg=back_ground)
            frame_imagem.place(x=100, y=80)

        # clear moves
        for widget in window.winfo_children():
            if isinstance(widget, Label) and 290 <= widget.winfo_x() <= 450 and widget.winfo_y() >= 360:
                widget.destroy()

        # add new moves
        new_moves = new_information['moves'][:3]
        for idx, movimento_info in enumerate(new_moves):
            move_name = movimento_info['move']['name'].replace("-", " ").title()
            pokemon_move = Label(window,
                text=f"• {move_name}",
                relief="flat",
                anchor='w',
                font=("lvy 10"),
                bg=co1,
                fg=co0)
            pokemon_move.place(x=290, y=400 + idx * 30)

    except requests.exceptions.ConnectionError:
        description_frame.config(text="❌ Connection error.\nCheck your internet connection.")
        frame_imagem.config(image=None, text="❌ No connection", font=("lvy 10"), fg="red", bg=co7)
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

#input
entry_pokemon = Entry(window, font=("verdana 12"), width=20, bg=co1, fg=co0, relief="solid")
entry_pokemon.bind('<Return>', lambda event: new_pokemon()) #Enter
entry_pokemon.place(x=300, y=10)

botao_buscar = Button(window,
    text="Search",
    command=new_pokemon,
    font=("verdana 10 bold"),
    bg=co5,
    fg=co1,
    relief="raised",
    overrelief=RIDGE)

botao_buscar.place(x=460, y=9)

if __name__ == "__main__":
    window.mainloop()