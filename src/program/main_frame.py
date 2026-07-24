from tkinter import CENTER, Label

co0 = "#09090C"
co1 = "#feffff"
co5 = "#ef5350"
co7 = "#a5e286"

def main_frame(texto=None, fonte=None, bg=None, anchor=None, relief="flat", master=None, frame_pokemon=None, **kwargs):
    if master is None:
        master = frame_pokemon

    label = Label(
        master,
        text=f"{texto}".capitalize(),
        relief=relief,
        anchor=CENTER if anchor is None else anchor,
        font=("lvy 10 bold") if fonte is None else fonte,
        bg=co7 if bg is None else bg,
        fg=co0
    )

    for key, value in kwargs.items():
        label[key] = value

    return label