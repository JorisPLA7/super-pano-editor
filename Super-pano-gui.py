appVersion ="0.2.3"
rectFill='pink'
test = 121212
helppage = "https://github.com/Kouskali/super-pano-editor/blob/master/README.md"
githubpage = "https://github.com/Kouskali/super-pano-editor/"
cachedata = "DEFAULTS ! ! !"
def rfcbutton():
   cachedata = datasheets.readfilecontent()
   print(cachedata)
   
def wfcbutton():
   datasheets.writefilecontent(cachedata)

def donothing():
   filewin = Toplevel(root)
   button = Button(filewin, text="Do nothing button")
   button.pack()
   print("#############################")
   
   
def refreshCanvas(rectFill):
   
   print("coucou")
   root.mainloop()
   w.delete()
   rectangle = w.create_rectangle(0, 0, 200, 300, fill=rectFill)
   rectangle = w.create_rectangle(0, 0, 200, 300, fill=rectFill)
   w.create_line(0, 0, 200, 300)
   w.create_line(0, 300, 200, 0, fill="red", dash=(4, 4))
   print("canvas actualisé avec succès !")

def validation():
	refreshCanvas(saisieRectFill.get())
	
# def refreshCanvas():
#     w.delete()
#     rectangle = w.create_rectangle(0, 0, 200, 300, fill=rectFill)
#     rectangle = w.create_rectangle(0, 0, 200, 300, fill=rectFill)
#     w.create_line(0, 0, 200, 300)
#     w.create_line(0, 300, 200, 0, fill="red", dash=(4, 4))
#     print("canvas actualisé avec succès")
#     root.mainloop()

## init tkinter
from tkinter import *
from lib import graphiti
from lib import web
from lib import datasheets
from tkinter.filedialog import *
import pickle
from tkinter.messagebox import askokcancel, askyesno,askquestion
root=Tk()




##Menubar
menubar = Menu(root)

filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Nouveau", command=donothing)
filemenu.add_command(label="Ouvrir une sauvegarde", command=rfcbutton)
filemenu.add_command(label="Sauvegarder", command=wfcbutton)
filemenu.add_separator()
filemenu.add_command(label="Quitter", command=root.destroy)
menubar.add_cascade(label="Fichier", menu=filemenu)

helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="Version de l'application : {}".format(appVersion), command=web.help)
helpmenu.add_command(label="Ouvrir une aide sur le web", command=web.help)
menubar.add_cascade(label="Aide", menu=helpmenu)

devmenu = Menu(menubar, tearoff=0)
devmenu.add_command(label="fonction print test", command=graphiti.joris)
menubar.add_cascade(label="Developpement", menu=devmenu)

root.config(menu=menubar)

##header
header = Label(root, text="Outil de configuration du trépied. Version {}".format(appVersion))
header.pack(fill="both", expand="no")

##aside frame
aside = Frame(root)
aside.pack(side=LEFT)

##init canvas
w = Canvas(aside, width=200, height=300)
w.pack()


##panneau  trans
translatif = LabelFrame(root, text="Module translatif")
translatif.pack(fill="both", expand="yes", side=TOP)
 
left = Label(translatif, text="PEW")
left.pack()


##panneau  rotat°
rotatif = LabelFrame(root, text="Module rotatif")
rotatif.pack(fill="both", expand="yes", side=TOP)

left = Label(rotatif, text="coup de 12")
left.pack()
    ##panneau  couleur select
couleur = Frame(rotatif, relief=GROOVE)
couleur.pack()

coulLabel = Label(couleur, text="couleur rectangle :")
coulLabel.pack(side=LEFT, padx=80, pady=20)
saisieRectFill=Entry(couleur)
saisieRectFill.pack(side=LEFT, padx=80,pady=20)

rectFill = saisieRectFill.get()


boutonQuestion = Button(root, text="valider", command=validation)
boutonQuestion.pack(side=BOTTOM)







root.mainloop()


'''
lab = Label(root, text="Saisir votre texte ici :")
lab.pack(side=LEFT, padx=80, pady=20)
saisie=Entry(root)
saisieRectFill.pack(side=LEFT, padx=80,pady=20)




boutonOK = Button(root,text="Fen ok:annuler", command=comOk)
boutonOK.pack(side=BOTTOM)
boutonQuestion = Button(root, text="Fen ask question", command= comQuestion)
boutonQuestion.pack()
boutonOui =Button(root, text = "fenêtre oui/non", command = comOui)
boutonOui.pack()



'''






