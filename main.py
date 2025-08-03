from tkinter import *
from tkinter import ttk

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

frame_nome = Label(frame_pokemon, text="Typlotion", relief="flat", anchor=CENTER, font=("Fixedsys 20 bold"),bg=co1,fg=co0)
frame_nome.place(x=12, y=15)

frame_tipo = Label(frame_pokemon, text="fogo", relief="flat", anchor=CENTER, font=("lvy 10 bold"),bg=co1,fg=co0)
frame_tipo.place(x=12, y=50)

frame_id = Label(frame_pokemon, text="#75", relief="flat", anchor=CENTER, font=("lvy 10 bold"),bg=co1,fg=co0)
frame_id.place(x=12, y=75)

janela.mainloop()