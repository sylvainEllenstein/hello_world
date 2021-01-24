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
    return sum([plateau[i][x_array[i]] for i in range(len(x_array))])
				   
def cases_suivantes(x):
    #retourne les cases suivantes possibles à partir de l'abscisse d'une case quelconque
    if x == 0: return [0, 1]
    elif x == m - 1: return [m - 2, m - 1]
    return [x - 1, x, x + 1]

def meilleurChemin():
    #donne le(s) meilleur(s) chemin(s) actuel(s) dans tous les chemins
    return [i for i,x in enumerate(liste_poids) if x == min(liste_poids)]

def meilleureCase(x_array):
 	#calcule les prochaines meilleures cases d'un chemin
    suivantes = cases_suivantes(x_array[::-1][0])
    valeurs = [plateau[len(x_array)][i] for i in suivantes] 
    return [suivantes[i] for i in range (0, len(suivantes)) if valeurs[i] == min(valeurs)]


def copieChemin(chemin_init, case):
    # copie un chemin existant (x_array) en rajoutant la case 'case'
    # l'envoye dans la bonne liste, si le chemin est terminé ou non
    # actualise les poids si un chemin n'est pas terminé
    global solutions
    global liste_poids
    global liste_chemins

    chemin_init.append(case)
    if len(chemin_init) == n:
    	solutions.append(chemin_init)
    	print(chemin_init, case)
    else :
    	liste_chemins.append(chemin_init)
    	liste_poids.append(poids(chemin_init))

def nouveauxChemins(x_array):
    #entrée : un chemin (x_array)
    # -> créé avec copieChemin() les nouveaux x_arrays, directement dans les listes solutions ou liste_chemins
    # remet le chemin initial si longueur < n - 1
    #type(out) : None
    if len(x_array) < n - 1:
        print(f"again added array : {x_array}")
        liste_chemins.append(x_array)
        liste_poids.append(poids(x_array))
    

    try :
        cases = meilleureCase(x_array)
    except :
        print(x_array)
    for case in cases: 
        if poids(x_array) + plateau[len(x_array)][case] <= a:
            copieChemin(x_array, case)

end = (liste_chemins == [])

while not end:
    #prendre le plus court chemin, le continuer (ne pas supprimer l'original) -> OU suppresion dans poids et dans chemins
    for x in meilleurChemin(): #type : list[int]
        del(liste_poids[x])
        nouveauxChemins(liste_chemins.pop(x))


if solutions == []:
    stdout.write("IMPOSSIBLE")	
else : # si il y a des solutions
    display(solutions[0])
    for chemin in solutions[1:]:
    	stdout.write("ou\n")
    	display(chemin)

"""
12
4
4
4 4 3 4
3 5 5 4
2 4 5 3
4 3 2 5

5
3
3
1 2 3
4 5 6
7 8 9
"""
