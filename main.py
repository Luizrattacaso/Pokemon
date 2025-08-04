from tkinter import *
from tkinter import ttk

from PIL import Image, ImageTk

from utils import get_pokemon_info, description

#pokemon inicial
name = "dragonite"
pokemon_info = get_pokemon_info(name.lower())

co0 = "#09090C"
co1 = "#feffff"
co5 = "#ef5350"
co6 = "#7C5AD2"

janela = Tk()
janela.title("Pokemons")
janela.geometry("550x510")
janela.resizable(False, False)

try:
    icone = PhotoImage(file="images/cabeca-pikachu.png")
    janela.iconphoto(False,icone)
except:
    pass

janela.config(bg=co1)

ttk.Separator(janela, orient= HORIZONTAL).grid(row=0,columnspan=1, ipadx=272)

style = ttk.Style(janela)
style.theme_use("clam")

frame_pokemon = Frame(janela, width= 550, height = 290, relief="flat", background=co6)
frame_pokemon.grid(row=1,column=0)

frame_nome = Label(frame_pokemon,
    text=f"{pokemon_info["name"]}".capitalize(),
    relief="flat",
    anchor=CENTER,
    font=("Fixedsys 20 bold"),
    bg=co6,
    fg=co0)
frame_nome.place(x=12, y=15)

frame_tipo = Label(frame_pokemon,
    text=f"{pokemon_info["types"][0]["type"]["name"]}".capitalize(),
    relief="flat",
    anchor=CENTER,
    font=("lvy 10 bold"),
    bg=co6,
    fg=co0)
frame_tipo.place(x=12, y=50)

frame_id = Label(frame_pokemon,
    text=f"#{pokemon_info["id"]}",
    relief="flat",
    anchor=CENTER,
    font=("lvy 10 bold"),
    bg=co6,
    fg=co0)
frame_id.place(x=12, y=75)

description_frame = Label(frame_pokemon,
    text=f"{description(name)}",
    anchor=NW,
    font=("lvy 12"),
    bg=co6,
    fg=co0,
    justify="left",
    wraplength=150)  # quebra de linha
description_frame.place(x=375, y=100)

description_frame.lift()

#imagens
imagem_pokemon = Image.open("images/dragonite.png")
imagem_pokemon = imagem_pokemon.resize((220,220))
imagem_pokemon = ImageTk.PhotoImage(imagem_pokemon)

frame_imagem= Label(frame_pokemon,image = imagem_pokemon, bg=co6,fg=co0)
frame_imagem.place(x=60, y=50)

frame_tipo.lift() #o método lift sobrepõe o que estamos usando como referencia

#status
status_pokemon = Label(janela,
    text="Informations",
    relief="flat",
    anchor=CENTER,
    font=("verdana 20 bold"),
    bg=co1,
    fg=co0)
status_pokemon.place(x="15", y="310")

altura_pokemon = Label(janela, text=f"• Height: {pokemon_info["height"]}", relief="flat", anchor=CENTER, font=("lvy 10"),bg=co1,fg=co0)
altura_pokemon.place(x="15", y="365")

peso_pokemon = Label(janela,
    text=f"• Weight: {pokemon_info["weight"]}",
    relief="flat",
    anchor=CENTER,
    font=("lvy 10"),
    bg=co1,
    fg=co0)
peso_pokemon.place(x="15", y="385")

#moves
moves_pokemon = Label(janela,
    text="Moves",
    relief="flat",
    anchor=CENTER,
    font=("verdana 20 bold"),
    bg=co1,
    fg=co0)
moves_pokemon.place(x="285", y="310")

movimentos = pokemon_info['moves'][:5]  #5 movimentos

for idx, movimento_info in enumerate(movimentos):
    nome_movimento = movimento_info['move']['name'].replace("-", " ").title()
    movimento_pokemon = Label(janela,
    text=f"• {nome_movimento}",
    relief="flat",
    anchor='w',
    font=("lvy 10"),
    bg=co1,
    fg=co0)

    movimento_pokemon.place(x=290, y=360 + idx * 30)

pokemon_1 = Image.open("images/cabeca-dragonite.png")
pokemon_1 = pokemon_1.resize((35,35))
pokemon_1 = ImageTk.PhotoImage(pokemon_1)


def new_pokemon():
    new_pokemon_name = entry_pokemon.get().strip().lower()
    if not new_pokemon_name:
        return
    
    try:
        novo_info = get_pokemon_info(new_pokemon_name)
        nova_desc = description(new_pokemon_name)
        nova_desc = nova_desc.replace('\n', ' ').replace('\f', ' ')

        cores_tipos = {
            "normal": "#A8A77A",
            "fighting": "#C22E28",
            "flying": "#A9D4F0",
            "poison": "#B763CD",
            "ground": "#E2BF65",
            "rock": "#B6A136",
            "bug": "#A2D97C",
            "ghost": "#755793",
            "steel": "#C5CBA3",
            "fire": "#EE8130",
            "water": "#6390F0",
            "grass": "#7AC74C",
            "electric": "#F7D02C",
            "psychic": "#F95587",
            "ice": "#96D9D6",
            "dragon": "#7C5AD2",
            "dark": "#705746",
            "fairy": "#D685AD",
            "stellar": "#6A4C9C",
            "unknown": "#DFC570"
        }

        tipo = novo_info["types"][0]["type"]["name"]
        cor_fundo = cores_tipos.get(tipo.lower(), "#FFFFFF")
        
        #labels
        frame_pokemon.config(bg=cor_fundo)
        frame_nome.config(text=novo_info["name"].capitalize(),bg=cor_fundo)
        frame_tipo.config(text=tipo.capitalize(),bg=cor_fundo)
        frame_id.config(text=f"#{novo_info['id']}", bg=cor_fundo)
        description_frame.config(text=nova_desc, bg=cor_fundo)
        altura_pokemon.config(text=f"• Height: {novo_info['height']}")
        peso_pokemon.config(text=f"• Weight: {novo_info['weight']}")

        #imagem
        nova_imagem = Image.open(f"images/{new_pokemon_name}.png")
        nova_imagem = nova_imagem.resize((220,220))
        nova_imagem = ImageTk.PhotoImage(nova_imagem)
        frame_imagem.config(image=nova_imagem, bg=cor_fundo)
        frame_imagem.image = nova_imagem  # manter referência

        #moves
        for widget in janela.winfo_children():
            if isinstance(widget, Label) and widget.winfo_y() >= 360 and widget.winfo_x() >= 290:
                widget.destroy()

        novos_moves = novo_info['moves'][:5]
        for idx, movimento_info in enumerate(novos_moves):
            nome_movimento = movimento_info['move']['name'].replace("-", " ").title()
            movimento_pokemon = Label(janela,
                text=f"• {nome_movimento}",
                relief="flat",
                anchor='w',
                font=("lvy 10"),
                bg=co1,
                fg=co0)
            movimento_pokemon.place(x=290, y=360 + idx * 30)

    except Exception as e:
        description_frame.config(text="Pokemon not found.")
        print(f"Error: {e}")

#entrada
entry_pokemon = Entry(janela, font=("verdana 12"), width=20, bg=co1, fg=co0, relief="solid")
entry_pokemon.place(x=300, y=10)

botao_buscar = Button(janela,
    text="Search",
    command=new_pokemon,
    font=("verdana 10 bold"),
    bg=co5,
    fg=co1,
    relief="raised",
    overrelief=RIDGE)
botao_buscar.place(x=460, y=7)

janela.mainloop()