from tkinter.filedialog import *

def open():
    filepath = askopenfilename(title="Ouvrir un fichier de configuration",filetypes=[('configuration super pano','.pano'),('all files','.*')])
    photo = PhotoImage(file=filepath)
    canvas = Canvas(fenetre, width=photo.width(), height=photo.height(), bg="yellow")
    canvas.create_image(0, 0, anchor=NW, image=photo)
    canvas.pack()