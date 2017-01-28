from tkinter.filedialog import *
import pickle

<<<<<<< HEAD
def getfilepath(head):
    filepath = askopenfilename(title=head,filetypes=[('configuration super pano','.supano'),('all files','.*')])
    return filepath
    
def readfilecontent():

    Fichier = open(getfilepath("Ouvrir un fichier de configuration"),'r')
    cachedata = Fichier.read()
    return cachedata
    
    
def writefilecontent(cachedata):

    Fichier = open(getfilepath("Enregistrer un fichier de configuration"),'w')
    Fichier.write(cachedata)
=======
def readfilecontent():
	filepath = askopenfilename(title="Ouvrir une configuration",filetypes=[('configuration super pano','.supano'),('all files','.*')])
	
	Fichier = open(filepath,'r')
	cachedata = Fichier.read()
	
	Fichier.close()
	return cachedata
	
def writefilecontent(cachedata):
	filepath = asksaveasfilename(title="Sauveagrder une configuration",filetypes=[('configuration super pano','.supano'),('all files','.*')])
	
	
	try:
		Fichier = open(filepath,'w')
		Fichier.write(cachedata)
		Fichier.close()
	except FileNotFoundError:
		print("Erreure; Ecriture impossible !")
	else:
		print("Fichier ecrasé avec succes !")
		fh.close()


def pickwrite(cachedata):
	filepath = asksaveasfilename(title="Sauveagrder une configuration",filetypes=[('configuration super pano','.supano'),('all files','.*')])
	with open(filepath, 'wb') as Fichier:
		mon_pickler = pickle.Pickler(Fichier)
		mon_pickler.dump(cachedata)
	print('ecriture du fichier effectuée avec succès.')


def pickread():
	filepath = askopenfilename(title="Ouvrir une configuration",filetypes=[('configuration super pano','.supano'),('all files','.*')])
	Fichier = open(filepath, 'rb') 
	cachedata = pickle.load(Fichier) 
	return cachedata
#pick()
>>>>>>> parent of b0bf4b7... fini  :+1:
