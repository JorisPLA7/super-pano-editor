##PROGRAMME SOUS LISCENCE G.P.L ........ Joris Placette ........ 2017

global appVersion
appVersion = "0.3.4 revival"
rectFill='pink'
test = 121212
helppage = "https://github.com/Kouskali/super-pano-editor/blob/master/README.md"
githubpage = "https://github.com/Kouskali/super-pano-editor/"

cachedata = {
"angleinter":    0,
"angletotal":   0,
"posx":   0,
"versys":   appVersion,
}

##buttons
def rbfcbutton():
   global cachedata
   datatampon = cachedata
   cachedata = datasheets.pickread()
   if cachedata["versys"] == "fail!":
      cachedata = datatampon
   print("nouvelles données en ram: {}".format(cachedata))
   
def wbfcbutton():
   if int(saisieangleinter.get()) > 50:
      guierror("l'angle entre 2 position doit être compris entre 0 et 50° !")
   else:
      pulldata()
      datasheets.pickwrite(cachedata)

##data treatment
def pulldata():
   cachedata["angletotal"] = saisieangletotal.get()
   cachedata["angleinter"] = saisieangleinter.get()   
   cachedata["posx"] = saisieposx.get()

##external fcts
def donothing():
   filewin = Toplevel(root)
   button = Button(filewin, text="Do nothing button")
   button.pack()
   print("Fenêtre qui ne fait rien ouverte")
   
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

##gui
def guierror(reason):
   errorframe = LabelFrame(root, text="Il y a un problème :'(  !", fg="red" )
   errorframe.pack(fill="both", expand="no", side=BOTTOM)
   
   destroybutton= Button(errorframe, text="x", command=errorframe.destroy)
   destroybutton.pack(side=LEFT)
   
   left = Label(errorframe, text=reason, fg="red")
   left.pack()
   
   root.mainloop()
 

## init tkinter
from tkinter import *
from lib import graphiti
from lib import web
from lib import datasheets
from tkinter.filedialog import *
import pickle
from tkinter.messagebox import askokcancel, askyesno,askquestion
root=Tk()

root.wm_title('Super Pano GUI')
root.wm_iconbitmap('ressources\supano.ico')




##Menubar
menubar = Menu(root)

filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Nouveau", command=donothing)
filemenu.add_command(label="Ouvrir une sauvegarde", command=rbfcbutton)
filemenu.add_command(label="Sauvegarder", command=wbfcbutton)
filemenu.add_separator()
filemenu.add_command(label="Quitter", command=root.destroy)
menubar.add_cascade(label="Fichier", menu=filemenu)

helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="Version de l'application : {}".format(appVersion), command=web.help)
helpmenu.add_command(label="Ouvrir une aide sur le web", command=web.help)
menubar.add_cascade(label="Aide", menu=helpmenu)

devmenu = Menu(menubar, tearoff=0)
# devmenu.add_command(label="fonction print test", command=graphiti.joris)
# devmenu.add_command(label="pick write", command=wbfcbutton)
# devmenu.add_command(label="pick read", command=rbfcbutton)
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
 
left = Label(translatif, text="Position linéaire :")
left.pack()

saisieposx = Spinbox(translatif, from_=0, to=100,)
saisieposx.pack()

#posx = saisieposx.get()

##panneau  rotat°
rotatif = LabelFrame(root, text="Module rotatif")
rotatif.pack(fill="both", expand="yes", side=TOP)

   ## pann subrotat1
subrotatif1 = Frame(rotatif)
subrotatif1.pack(fill="both", expand="yes", side=TOP)
   
titreangleinter = Label(subrotatif1, text="angle entre deux positions (degrés) :")
titreangleinter.pack()

saisieangleinter = Spinbox(subrotatif1, from_=0, to=50)
saisieangleinter.pack()
#cachedata["angleinter"] = saisieangleinter.get()   

   ## pann subrotat2
subrotatif2 = Frame(rotatif)
subrotatif2.pack(fill="both", expand="yes", side=TOP)
   
titreangletotal = Label(subrotatif2, text="angle total du mouvement (degrés) :")
titreangletotal.pack()

saisieangletotal = Spinbox(subrotatif2, from_=0, to=50)
saisieangletotal.pack()

#cachedata["angletotal"] = saisieangletotal.get()

   ##panneau  couleur select
couleur = Frame(rotatif, relief=GROOVE)
couleur.pack()

coulLabel = Label(couleur, text="couleur rectangle :")
coulLabel.pack(side=LEFT, padx=80, pady=20)
saisieRectFill=Entry(couleur)
saisieRectFill.pack(side=LEFT, padx=80,pady=20)

rectFill = saisieRectFill.get()


savebutton= Button(root, text="enregistrer", command=wbfcbutton)
savebutton.pack()

root.mainloop()






