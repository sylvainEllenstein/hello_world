from sys import stdin, stdout

stdin.readline = input

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

liste_chemins = [[_] for _ in range (0, m)] #décrit les chemins étudiés : list(list(int)) -> abscisses des cases des chemins
liste_poids = [i for i in plateau[0]] #poids qui correspondent aux chemins dans liste_chemins
solutions = [] 

def display(x_array):
    #affiche un chemin, saute une ligne à la fin
    stdout.write(f"{x_array[0]}")
    for i in x_array[1:]:
        stdout.write(f" {i}")
    stdout.write("\n")

def poids(x_array):
	#poids d'un chemin
    return sum([plateau[i][x_array[i]] for i in range(len(x_array))])
				   
def cases_suivantes(x):
    #retourne les cases suivantes possibles à partir de l'abscisse d'une case quelconque
    if x == 0: return [0, 1]
    elif x == m - 1: return [m - 2, m - 1]
    return [x - 1, x, x + 1]

def meilleurChemin():
    #donne le meilleur chemin actuel dans tous les chemins
    #si plusieurs ont le même poids : un seul sera sélectionné (premier) mais ne change rien à priori
    return liste_poids.index(min(liste_poids))

def nouveauxChemins(x_array):
    #entrée : un chemin (x_array)
    # -> visite tous les chemins suivants qui ne dépassent pas le seuil 'âme du visiteur'
    global solutions
    global liste_poids
    global liste_chemins

    if len(x_array) == n - 1: #si le chemin est sur le point de se terminer
    	for i in cases_suivantes(x_array[::-1][0]): # TOUTES les cases suivantes
    		if poids(x_array) + plateau[len(x_array)][i] <= a: # si le poids du chemin est assez bas
    			solutions.append(x_array + [i]) # on ajoute le chemin aux solutions

    else :
    	for i in cases_suivantes(x_array[::-1][0]): 
    		if poids(x_array) + plateau[len(x_array)][i] < a:
    			liste_chemins.append(x_array + [i])
    			liste_poids.append(poids(x_array) + plateau[len(x_array)][i])


end = (liste_chemins == [])

while not end:
    try :
        x = meilleurChemin()
        del(liste_poids[x])
        nouveauxChemins(liste_chemins.pop(x))
    except :
        end = True
        
if solutions == []:
    stdout.write("IMPOSSIBLE")	
else : # si il y a des solutions
    display(solutions[0])
    for chemin in solutions[1:]:
    	stdout.write("ou\n")
    	display(chemin)

#BILAN:
# Après tentatives en récursif(l'affichage était rigoureusement identique mais marquait pourtant une erreur... ???), essai en itératif
# l'affichage du programme semble correspondre à celui demandé sur Prologin
#PROBLEMES / Sources d'erreur possibles :
# -> trop lent/ utilisation abusive de mémoire
