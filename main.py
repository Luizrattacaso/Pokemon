from tkinter import *
from tkinter import ttk

from PIL import Image, ImageTk

from pokemon import get_pokemon_info

name = "dragonite"
pokemon_info = get_pokemon_info(name.lower())

co0 = "#444466"
co1 = "#feffff"
co2 = "#6f9fbd"
co3 = "#38576b"
co4 = "#403d3d"
co5 = "#ef5350"

janela = Tk()
janela.title("teste")
janela.geometry("550x510")
janela.config(bg=co1)

ttk.Separator(janela, orient= HORIZONTAL).grid(row=0,columnspan=1, ipadx=272)

style = ttk.Style(janela)
style.theme_use("clam")

frame_pokemon = Frame(janela, width= 550, height = 290, relief="flat")
frame_pokemon.grid(row=1,column=0)

frame_nome = Label(frame_pokemon, text=f"{pokemon_info["name"]}".capitalize(), relief="flat", anchor=CENTER, font=("Fixedsys 20 bold"),bg=co1,fg=co0)
frame_nome.place(x=12, y=15)

frame_tipo = Label(frame_pokemon, text=f"{pokemon_info["types"][0]["type"]["name"]}".capitalize(), relief="flat", anchor=CENTER, font=("lvy 10 bold"),bg=co1,fg=co0)
frame_tipo.place(x=12, y=50)

frame_id = Label(frame_pokemon, text=f"#{pokemon_info["id"]}", relief="flat", anchor=CENTER, font=("lvy 10 bold"),bg=co1,fg=co0)
frame_id.place(x=12, y=75)

#imagens
imagem_pokemon = Image.open("/home/luiz/Imagens/images/pikachu.png")
imagem_pokemon = imagem_pokemon.resize((220,220))
imagem_pokemon = ImageTk.PhotoImage(imagem_pokemon)

frame_imagem= Label(frame_pokemon,image = imagem_pokemon, bg=co1,fg=co0)
frame_imagem.place(x=60, y=50)

frame_tipo.lift() #o método lift sobrepõe o que estamos usando como referencia

#status
status_pokemon = Label(janela, text="Informations", relief="flat", anchor=CENTER, font=("verdana 20 bold"), bg=co1, fg=co0)
status_pokemon.place(x="15", y="310")

altura_pokemon = Label(janela, text=f"• Height: {pokemon_info["height"]}", relief="flat", anchor=CENTER, font=("lvy 10"),bg=co1,fg=co0)
altura_pokemon.place(x="15", y="365")

peso_pokemon = Label(janela, text=f"• Weight: {pokemon_info["weight"]}", relief="flat", anchor=CENTER, font=("lvy 10"),bg=co1,fg=co0)
peso_pokemon.place(x="15", y="385")

#habilidades
moves_pokemon = Label(janela, text="Moves", relief="flat", anchor=CENTER, font=("verdana 20 bold"), bg=co1, fg=co0)
moves_pokemon.place(x="285", y="310")

movimentos = pokemon_info['moves'][:5]  #5 movimentos

for idx, movimento_info in enumerate(movimentos):
    nome_movimento = movimento_info['move']['name'].replace("-", " ").title()
    movimento_pokemon = Label(janela, text=f"• {nome_movimento}", relief="flat", anchor='w', font=("lvy 10"), bg=co1, fg=co0)
    movimento_pokemon.place(x=290, y=360 + idx * 30)
    
#botao

janela.mainloop()