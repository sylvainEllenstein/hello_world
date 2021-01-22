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
	
    liste_chemins = [[_] for _ in range (0, m)] #décrit les chemins étudiés : list(list(int)) -> abscisses des cases des chemins
	liste_poids = [plateau[0][i] for i in plateau[0]] #poid qui correspondent aux chemins dans liste_chemins
    
	def poids(x_array, plateau):
		#retourne le poids d'un array
		#type(out) : int
		return sum([plateau[i][x_array[i]] for i in range(len(x_array))]
				   
    def cases_suivantes(x, largeur):
        #retourne les cases suivantes d'un chemin 
        if x == 0: return [0, 1]
    	elif x == largeur - 1: return [largeur - 1, largeur]
        return [x - 1, x, x + 1]
    
    def meilleurChemin(poids):
        #donne le(s) meilleur(s) chemin(s) actuel(s) dans tous les chemins
        #type(out) : list(int) -> place des chemins dans liste_chemins
        return [i for i,x in enumerate(poids) if x == min(poids)]
    
	def meilleureCase(x_array,plateau, m):
    	#calcule la prochaine meilleure case d'un objet chemin
        #type(out) : list(int) -> x
		suivantes = cases_suivantes(x_array[::-1][0], m)
		valeur = lambda x : plateau[len(x_array)][x]
		meilleures = [i for i in suivantes if valeur[i] == min(list(valeur(x) for x in suivantes))]

	def copieChemin(chemin_init, case):
		#copie un chemin existant en rajoutant la case 'case'
		chemin_init.append(case)
		global liste_chemins
		liste_chemins.append(chemin_init)
		liste_poids.append(poids(chemin_init))
	
	def nouveauxChemins(x_array):
		#entrée : le chemin à continuer (choisi par meilleurChemin dans le main)
		# -> continue / créé de nouveaux x_arrays (avec copieChemin) si nécessaire
		# -> coupe les chemins créés trop grands
		global a #ame du visiteur
		
				   
    def main():      
        #TODO : boucle qui prend le plus court objet chemin, le continue et actualise sa longueur
        #la boucle coupe si le plus court chemin est plus grand que l'âme du visiteur, et coupe les chemins créés déjà trop grands
		global liste_chemins
		global a
		global m
		global n
		global plateau
		global liste_poids
				   
				   
        mainloop = ((max[(len(i)) for i in liste_chemins] < n) or ( #si le chemin qui a atteint le bord n'est pas le plus court
		)) and (meilleurChemin(liste_poids) <= a) 
		#tant que le plus court chemin n'est pas trop grand ------> si liste_chemins == []
		#aucun chemin chemin n'atteint le bord ou si le chemin qui a atteint le bord n'est pas le plus court
		
		while mainloop:
			#continue un chemin SI : plus court ET non-fini
			# + actualiser les pooids
			# + couper les chemins si déjà trop grands (créer les chemins un par un)
			pass
			mainloop = False
		
	main()
    
        
labyrinthe_demoniaque()
