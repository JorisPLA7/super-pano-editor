from tkinter.filedialog import *
import pickle

def pickwrite(cacheData):
	try:
		filepath = asksaveasfilename(title="Sauveagrder une configuration",filetypes=[('configuration super pano','.supano'),('all files','.*')]) #récupération de l'adresse à laquelle enregistrer le fichier
		with open(filepath, 'wb') as Fichier: #ouverture d'un Fichier , il sera automatiquement fermé à la fin de la boucle
			mon_pickler = pickle.Pickler(Fichier)
			mon_pickler.dump(cacheData)#ecriture des données dans le fichier
		print('ecriture du fichier  {}  effectuée avec succès.'.format(filepath))

	except:
		print("ecriture du fichier  {}  impossible !".format(filepath))

def pickread():
	global appVersion #réccupération de la variable globale (pour écriture)
	try:
		filepath = askopenfilename(title="Ouvrir une configuration",filetypes=[('configuration super pano','.supano'),('all files','.*')])#récupération de l'adresse à laquelle ouvrir le fichier
		Fichier = open(filepath, 'rb')
		cacheData = pickle.load(Fichier) #récupération
		Fichier.close() #fermeture du fichier

	except: #en cas d'érreur queconque
		print("lecture du fichier  {}  impossible".format(filepath))
		cacheData = {
		"angleinter":    0,
		"angletotal":   0,
		"posx":   0,
		"versys":   "fail!",
		} #valeurs par défaut
	else:
		print("lecture du fichier  {}  effectuée avec succès !".format(filepath))
	return cacheData #retourne la variable quand elle est appelée
