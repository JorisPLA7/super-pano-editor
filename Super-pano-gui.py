appVersion ="0.2.3"
rectFill='pink'
helppage = "https://github.com/Kouskali/super-pano-editor/blob/master/README.md"

def donothing():
   filewin = Toplevel(root)
   button = Button(filewin, text="Do nothing button")
   button.pack()
   print("#############################")
   
def refreshRotatif():
	global rectange
    print("coucou")
    rectFill = saisie.get()
    root.mainloop()
    w.delete()
    rectangle = w.create_rectangle(0, 0, 200, 300, fill=rectFill)
	rectangle = w.create_rectangle(0, 0, 200, 300, fill=rectFill)
	w.create_line(0, 0, 200, 300)
	w.create_line(0, 300, 200, 0, fill="red", dash=(4, 4))
	print("coucu")
    
def webopen():
    webbrowser.open(helppage)
## init tkinter
from tkinter import *
import webbrowser 
from tkinter.messagebox import askokcancel, askyesno,askquestion
root=Tk()




##Menubar
menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Nouveau", command=donothing)
filemenu.add_command(label="Ouvrir une sauvegarde", command=donothing)
filemenu.add_command(label="Sauvegarder", command=donothing)

filemenu.add_separator()

filemenu.add_command(label="Quitter", command=root.destroy)
menubar.add_cascade(label="File", menu=filemenu)

'''
editmenu = Menu(menubar, tearoff=0)
editmenu.add_command(label="Undo", command=donothing)

editmenu.add_separator()

editmenu.add_command(label="Cut", command=donothing)
editmenu.add_command(label="Copy", command=donothing)
editmenu.add_command(label="Paste", command=donothing)
editmenu.add_command(label="Delete", command=donothing)
editmenu.add_command(label="Select All", command=donothing)

menubar.add_cascade(label="Obtenir de l'aide", menu=editmenu)
'''
helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="Version de l'application : {}".format(appVersion), command=donothing)
helpmenu.add_command(label="Ouvrir une aide sur le web", command=webopen(helppage))
menubar.add_cascade(label="Aide", menu=helpmenu)

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


##panneau trans
translatif = LabelFrame(root, text="Module translatif")
translatif.pack(fill="both", expand="yes", side=TOP)
 
left = Label(translatif, text="PEW")
left.pack()

##panneau rotat°
rotatif = LabelFrame(root, text="Module rotatif")
rotatif.pack(fill="both", expand="yes", side=TOP)
 
left = Label(rotatif, text="coup de 12")
left.pack()

lab = Label(rotatif, text="couleur rectangle :")
lab.pack(side=LEFT, padx=80, pady=20)
saisie=Entry(rotatif)
saisie.pack(side=LEFT, padx=80,pady=20)

rectFill = saisie.get()


boutonQuestion = Button(rotatif, text="valider", command= refreshRotatif)
boutonQuestion.pack(side=BOTTOM)







root.mainloop()


'''
lab = Label(root, text="Saisir votre texte ici :")
lab.pack(side=LEFT, padx=80, pady=20)
saisie=Entry(root)
saisie.pack(side=LEFT, padx=80,pady=20)


def comOk():
    rep=askokcancel("fenêtre ok/cancel","Voulez-vous afficher la saisie ? ")
    if rep == True:
        print(" La valur saisie est :  "+saisie.get())

def comQuestion():
    rep = askquestion("fenêtre Nouvelle saisie", "voulez-vous continuer?")
    if rep=='yes':
        saisie.delete(0,END) # de char 0 à char final 
    if rep=='no':
        root.quit()
    
def comOui():
    rep = askyesno("alors?", "voulez-vous contiuer ?",icon='warning')
    if rep== False:
        root.quit()
        
        
        
boutonOK = Button(root,text="Fen ok:annuler", command=comOk)
boutonOK.pack(side=BOTTOM)
boutonQuestion = Button(root, text="Fen ask question", command= comQuestion)
boutonQuestion.pack()
boutonOui =Button(root, text = "fenêtre oui/non", command = comOui)
boutonOui.pack()

        

'''






