#coding=utf-8
class Joueur:
	score=100
	def __init__(self, name):
		self.name=name
		

def Result(a,valeur,valeurchoisie):
	if (valeur==valeurchoisie): 
		resultat=True
	else :
		resultat=False
		a.score=a.score-25
	return (resultat)

def Comparer(a, valeur,valeurchoisie):
	if (valeur<valeurchoisie):
		print(a.name+", le chiffre que vous avez choisi est inferieur")
		print("Essayez encore")

	elif (valeur>valeurchoisie):
		print(a.name+", le chiffre que vous avez choisi est superieur")
		print("Essayez encore")


		
def Jeu(a):
	choix=input("entrons le choix ")
	val=input("Entrez le nombre ") 
	while Result(a,val,choix) == False and a.score!=0:
		Comparer(a,val,choix)
		val=input("Entrez le nombre ") 
	if (a.score!=0):
		print("vous avez gagné")
	else:
		print("vous avez perdu score=0")

		
cisse=Joueur("zz")
Jeu(cisse)
Jeu(Joueur("Zeff"))
Jeu(Joueur("Dim"))