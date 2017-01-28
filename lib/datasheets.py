from tkinter.filedialog import *
import pickle

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
    with open('donnees', 'wb') as Fichier:
        mon_pickler = pickle.Pickler(Fichier)
        mon_pickler.dump(cachedata)
    print('ecriture du fichier effectuée avec succès.')

#pick()
