 def labyrinthe_demoniaque():
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

    a = int(input()) #ame du visiteur
    n = int(input()) #longueur
    m = int(input()) #largeur
    plateau = [list(map(int, input().split(" "))) for _ in range(n)]
	
    liste_chemins = [_] for _ in range (0, m) #décrit les chemins étudiés : list(list(int)) -> abscisses des cases des chemins
	liste_poids = [plateau[0][i] for i in plateau[0]] #poid qui correspondent aux chemins dans liste_chemins
    
	def poids(x_array, plateau):
		#retourne le poids d'un array
		#type(out) : int
		return sum([plateau[i][x_array[i]] for i in range(len(x_array))]
				   
    def cases_suivantes(x, largeur):
        #retourne les cases suivantes d'un objet chemin 
        if x == 0: return [0, 1]
    	elif x == largeur - 1: return [largeur - 1, largeur]
        return [x - 1, x, x + 1]
    
    def meilleurChemin(poids):
        #donne le(s) meilleur(s) chemin(s) actuel(s) dans tous les objets chemin
        #type(out) : list(int) -> x des chemins
        return [i for i,x in enumerate(poids) if x == min(poids)]
    
	def meilleureCase(x_array,plateau):
    	#calcule la prochaine meilleure case d'un objet chemin
        #type(out) : list(int) -> x
		return [plateau[len(x_array)][i] for i in cases_suivantes(x_array[::-1][0]]

				   
	def nouveauChemin(chemin_init, case):
		chemin_init.append(case)
		liste_chemins.append(chemin_init)
		liste_poids.append(poids(chemin_init))
	
    def main(chemins_possibles, plateau):        
        #TODO : boucle qui prend le plus court objet chemin, le continue et actualise sa longueur
        #la boucle coupe si le plus court chemin est plus grand que l'âme du visiteur, et coupe les chemins déjà trop grands
        mainloop = (() or ()) and (meilleurChemin(liste_poids) <= a): 
		#tant que le plus court chemin n'est pas trop grand + aucun chemin chemin n'atteint le bord ou si le chemin qui a atteint le bord n'est pas le plus court
		while mainloop:
			pass
			mainloop = False
		
		
		
        pass
    
        
labyrinthe_demoniaque()
