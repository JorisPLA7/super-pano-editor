from tkinter.filedialog import *
import pickle

def pickwrite(cachedata):
	try:
		filepath = asksaveasfilename(title="Sauveagrder une configuration",filetypes=[('configuration super pano','.supano'),('all files','.*')])
		with open(filepath, 'wb') as Fichier:
			mon_pickler = pickle.Pickler(Fichier)
			mon_pickler.dump(cachedata)
		print('ecriture du fichier  {}  effectuée avec succès.'.format(filepath))
		
	except:
		print("ecriture du fichier  {}  impossible !".format(filepath))
	
def pickread():
	global appVersion
	try:
		filepath = askopenfilename(title="Ouvrir une configuration",filetypes=[('configuration super pano','.supano'),('all files','.*')])
		Fichier = open(filepath, 'rb') 
		cachedata = pickle.load(Fichier) 
		Fichier.close()
	except:
		print("lecture du fichier  {}  impossible".format(filepath))
		cachedata = {
		"angleinter":    0,
		"angletotal":   0,
		"posx":   0,
		"versys":   "fail!",
		}
	else:
		print("lecture du fichier  {}  effectuée avec succès !".format(filepath))
	return cachedata
#pick()






