from tkinter import CENTER, Label

co0 = "#09090C"
co1 = "#feffff"

def frame_window(texto=None, fonte=None, bg=None, anchor=None, relief="flat", master=None, **kwargs):
    if master is None:
        raise RuntimeError("frame_window() requires a 'master' widget.")

    label = Label(
        master,
        text=f"{texto}".capitalize(),
        relief=relief,
        anchor=CENTER if anchor is None else anchor,
        font=("verdana 20 bold") if fonte is None else fonte,
        bg=co1 if bg is None else bg,
        fg=co0
    )

    for key, value in kwargs.items():
        label[key] = value

    return label