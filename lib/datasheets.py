from tkinter.filedialog import *
import pickle

def readfilecontent():
    filepath = askopenfilename(title="Ouvrir une configuration",filetypes=[('configuration super pano','.supano'),('all files','.*')])
    Fichier = open(filepath,'r')
    cachedata = Fichier.read()
    
    Fichier.close()
    return cachedata
    
def writefilecontent(cachedata):
    filepath = askopenfilename(title="Sauveagrder une configuration",filetypes=[('configuration super pano','.supano'),('all files','.*')])
    Fichier = open(filepath,'w')
    Fichier.write(cachedata)
    Fichier.close()

def pick(cachedata):
    with open('donnees', 'wb') as Fichier:
        mon_pickler = pickle.Pickler(Fichier)
        mon_pickler.dump(cachedata)
    print('ecriture du fichier effectuée avec succès.')

#pick()