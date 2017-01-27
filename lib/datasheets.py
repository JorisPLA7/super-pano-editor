from tkinter.filedialog import *
import pickle

def getfilepath():
    filepath = askopenfilename(title="Ouvrir un fichier de configuration",filetypes=[('configuration super pano','.supano'),('all files','.*')])
    return filepath
    
def getfilecontent():
    
    Fichier = open(getfilepath(),'r')
    print(Fichier)
    photo = PhotoImage(file=getfilepath())
    canvas = Canvas(fenetre, width=photo.width(), height=photo.height(), bg="yellow")
    canvas.create_image(0, 0, anchor=NW, image=photo)
    canvas.pack()