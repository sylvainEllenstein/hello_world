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

def poids(x_array):
    return sum([plateau[i][x_array[i]] for i in range(len(x_array))])


def cases_suivantes(x):
      #retourne les cases suivantes possibles à partir de l'abscisse d'une case quelconque
    global m
    if x == 0: return [0, 1]
    elif x == m - 1: return [m - 2, m - 1]
    return [x - 1, x, x + 1]




def meilleure_case(x_array):
    #retourne les meilleures cases suivantes d'un chemin décrit par un x_array (chemin)
    suivantes = cases_suivantes(x_array[::-1][0])
    valeurs = [plateau[len(x_array)][i] for i in suivantes]
    return [suivantes[i] for i in range(len(valeurs)) if valeurs[i] == min(valeurs)]

def chemins_rec(x_array):
    """
    Chemins en récursif à partir de la première case
    IN : [array]
    OUT : list[int]
    """
    
    if len(x_array) == m: #si chemin terminé
        return x_array

    else : 
        for i in meilleure_case(x_array):
            if plateau[len(x_array)][i] + poids(x_array) <= a:
                return chemins_rec(x_array + [i])

solutions = []
for i in range(m):
    #Try pour pallier temporairement à une erreur : lorsque pas de chemin possible à partir de la case, 
    #erreur car NoneType non itérable
    try : 
        solutions.append(list(chemins_rec([i])))
    except :
        pass   


#Affichage des solutions :

if solutions == []:
    stdout.write("IMPOSSIBLE\n")
else : 
    for i in solutions[0]:
        stdout.write(f"{i} ")
    stdout.write("\n")
    for chemin in solutions[1:]:
        stdout.write(" ou\n")
        for i in chemin:
            stdout.write(f"{i} ")
        stdout.write("\n")


 #BILAN :
 # - fonctionne sur les premiers tests, à priori
 #SOURCES D'ERREUR :
 # -> ne peut prendre en compte le cas où plusieurs chemin viennent d'une même case à cause du return dans chemins_rec
 # -> à tester avec yield dans une prochaine version, puis convertir le generator object
 
 
 
