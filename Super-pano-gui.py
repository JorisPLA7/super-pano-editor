##PROGRAMME SOUS LISCENCE G.P.L ........ Joris Placette ........ 2017

global appVersion

global palette

global posxmax 

posxmax = 200
appVersion = "0.3.5"
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
   datasheets.pickwrite(cachedata)
   
def verifbutton():
   nberror = 0
   if int(saisieangleinter.get()) < 0 or int(saisieangleinter.get()) > 50:
      guimessage("red", "Il y a un problème :'(  !", "l'angle entre 2 position doit être compris entre 0 et 50° !")
      nberror +=1
   if int(saisieangletotal.get()) < 0 or int(saisieangletotal.get()) > 720 :
      guimessage("red", "Il y a un problème :'(  !", "l'angle total doit être compris entre 0 et 720° !")
      nberror +=1
   
   if int(saisieposx.get()) < 0 or int(saisieposx.get()) > posxmax:
      guimessage("red", "Il y a un problème :'(  !", "La position linéaire doit être comprise entre 0 et {} !".format(posxmax))
      nberror +=1

   if nberror == 0:
      pulldata()
      refreshcanvas(cachedata)
      guivalidation()
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

def forcesave():
   print("tentative de sauvegarde forcée")
   pulldata()
   wbfcbutton()
   
   


##gui refreshers
def guimessage(color, context, reason):
   messageframe = LabelFrame(root, text=context, fg=color )
   messageframe.pack(fill="both", expand="no", side=BOTTOM)
   
   destroybutton= Button(messageframe, text="x", command=messageframe.destroy)
   destroybutton.pack(side=LEFT)
   
   left = Label(messageframe, text=reason, fg=color)
   left.pack()
   
   root.mainloop()

def guivalidation():
   validationframe = LabelFrame(root, text="Tout semble correct :) ", fg="green" )
   validationframe.pack(fill="both", expand="no", side=BOTTOM)
   
   destroybutton= Button(validationframe, text="x", command=validationframe.destroy)
   destroybutton.pack(side=LEFT)
   
   savebutton= Button(validationframe, text="enregistrer", command=wbfcbutton, fg="green")
   savebutton.pack()
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
filemenu.add_command(label="Sauvegarder sans validation", command=forcesave)
filemenu.add_separator()
filemenu.add_command(label="Quitter", command=root.destroy)
menubar.add_cascade(label="Fichier", menu=filemenu)

helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="Version de l'application : {}".format(appVersion), command=web.help)
helpmenu.add_command(label="Ouvrir une aide sur le web", command=web.help)
menubar.add_cascade(label="Aide", menu=helpmenu)

devmenu = Menu(menubar, tearoff=0)
# devmenu.add_command(label="fonction print test", command=graphiti.joris)
# devmenu.add_command(label="pick write", command=verifbutton)
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

def refreshcanvas(cachedata):   
   w.delete()
   rectangle = w.create_rectangle(10, 30, 190, 40, fill="white")
   
   posxdisp = int(int(cachedata["posx"]) / posxmax * 180 +10)
   
   w.create_line(posxdisp, 25, posxdisp, 45)
   angletotrest = cachedata["angletotal"]
   angleinterrest = cachedata["angleinter"]
   
   coord1 = 1, 50, 200, 170
   coord2 = 1, 60, 190, 160
   arctot = w.create_arc(coord1, start=10, extent=cachedata["angletotal"], fill="white")
   arcinter = w.create_arc(coord2, start=20, extent=cachedata["angleinter"], fill="black")

   print("canvas actualisé avec succès !")

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





checkbutton= Button(root, text="Verifier", command=verifbutton)
checkbutton.pack()


#verifbutton()
root.mainloop()






