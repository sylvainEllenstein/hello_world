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
    
	def poids(x_array):
		#retourne le poids d'un x_array
		#type(out) : int
		global plateau
		return sum([plateau[i][x_array[i]] for i in range(len(x_array))])
				   
    def cases_suivantes(x):
        #retourne les cases suivantes possibles à partir de l'abscisse d'une case, sans trier avec la meilleure

        global m
        if x == 0: return [0, 1]
    	elif x == m - 1: return [m - 1, m]
        return [x - 1, x, x + 1]


    def meilleurChemin(poids):
        #donne le(s) meilleur(s) chemin(s) actuel(s) dans tous les chemins
        #type(out) : list(int) -> place des chemins dans liste_chemins
        return [i for i,x in enumerate(poids) if x == min(poids)]

	def meilleureCase(x_array):
    	#calcule les prochaines meilleures cases d'un chemin
        #type(out) : list(int) -> les 'x' correspondant à la case en question
		suivantes = cases_suivantes(x_array[::-1][0]) # = les cases suivantes du chemin donné par x_array
		valeurs = [plateau[len(x_array)][i for i in suivantes]] #les valeurs des cases correspondant aux suivantes
		return [suivantes[i] for i in range (0, len(suivantes) if valeurs[i] == min(valeurs)]



	def copieChemin(chemin_init, case):
		#copie un chemin existant (x_array) en rajoutant la case 'case'
		#actualise les poids
		chemin_init.append(case)
		global liste_chemins
		liste_chemins.append(chemin_init)
		liste_poids.append(poids(chemin_init))
	
	def nouveauxChemins(x_array):
		#entrée : un chemin (x_array)
		# -> continue / créé de nouveaux x_arrays (avec copieChemin) si nécessaire
		# -> coupe les chemins créés trop grands
		#OUT : tous les chemins restants 
		#type(out) : -> void (???)
		global a #ame du visiteur
		if meilleureCase(x_array)[0] + poids(x_array) <= a:
			copieChemin(x_array, meilleureCase(x_array)[0])

		#boucle qui s'éxécute si il y a plusieurs cases suivantes possibles
		for i in meilleureCase(x_array)[1:]:
			if poids(x_array) + plateau[len(x_array)][i] <= a:
				copieChemin(x_array, i)


		
##################  MAIN  ##################################

    #TODO : boucle qui prend le plus court chemin
    # -> le supprime avec .pop() de liste_chemins
    # -> supprimer aussi le numéro de liste_poids correcpondant
    # -> envoyé à nouveauxChemins
    # -> .extend() sur liste_chemins des nouveauxChemins() du x_array
    # ...
				   
    mainloop = True 
 ##################  CONDITIONS MAINLOOP  ##################

    #si le chemin qui a atteint le bord n'est pas le plus court 
	#tant que le plus court chemin n'est pas trop grand ------> si liste_chemins == []
	#aucun chemin chemin n'atteint le bord ou si le chemin qui a atteint le bord n'est pas le plus court

 ###########################################################

	while mainloop:
		#continue un chemin SI : plus court (ET non-fini)
		# + actualiser les poids : se fait lors dela crétion/poursuite des chemins
		# + couper les chemins si déjà trop grands (créer les chemins un par un)
		# + deplacer les chemins validés dans une autre liste

		pass
		mainloop = False
		
	
    
        
labyrinthe_demoniaque()
