from sys import stdin, stdout

"""
:param a: ame du visiteur
:type a: int
:param n: longueur du labyrinthe
:type n: int
:param m: largeur du labyrinthe
:type m: int
:param plateau: grille du labyrinthe
:type plateau: list[list[int]]
"""
# TODO Retourne une liste d'entiers correspondant au meilleur chemin
# permettant de sortir du labyrinthe en conservant un maximum de son âme,
# sachant que le visiteur augmente sa coordonnée n à chaque case et ne peut
# revenir en arrière. Si aucun chemin n'est possible, afficher "IMPOSSIBLE"

a = int(stdin.readline()) #ame du visiteur
n = int(stdin.readline()) #longueur
m = int(stdin.readline()) #largeur
plateau = [list(map(int, stdin.readline().split(" "))) for _ in range(n)]


def cases_suivantes(x):
      #retourne les cases suivantes possibles à partir de l'abscisse d'une case quelconque
      global m
      if x == 0: return [0, 1]
      elif x == m - 1: return [m - 1, m]
      return [x - 1, x, x + 1]

def chemins_rec(x_array):
	"""
	Chemins en récursif à partir de la première case
	IN : [array]
	OUT : <generator object>
	"""
	
	if len(x_array) == m: #si chemin terminé
		yield x_array

	#sinon : 
	# -> regarde les cases_suivantes en fonctin de la dernière case du x_array
	# -> si la plus petite valeur fait dépasser le seuil a : abandon du x_array, pas de récursion dessus
	# -> sinon : on choisit les plus petites et on fait une récusrion dessus, avec un return 

###########  FONCTIONS SUPPLEMENTAIRES NECESSAIRES  #############

#cases_suivantes
# ??? poids ???
#

#################################################################

solutions = [list(chemins_rec([i])) for i in plateau[0]]




###########  AFFICHAGE DES CHEMINS REUSSIS  ############


########################################################
