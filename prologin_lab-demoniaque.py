 from sys import stdin, stdout

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

    a = int(stdin.readline()) #ame du visiteur
    n = int(stdin.readline()) #longueur
    m = int(stdin.readline()) #largeur
    plateau = [list(map(int, stdin.readline().split(" "))) for _ in range(n)]
	
    liste_chemins = [[_] for _ in range (0, m)] #décrit les chemins étudiés : list(list(int)) -> abscisses des cases des chemins
	liste_poids = [plateau[0][i] for i in plateau[0]] #poid qui correspondent aux chemins dans liste_chemins
    solutions = []

    def display(x_array):
    	for i in x_array:
    		stdout.write(f"{i} ")

	def poids(x_array):
		#retourne le poids d'un x_array
		#type(out) : int
		global plateau
		return sum([plateau[i][x_array[i]] for i in range(len(x_array))])
				   
    def cases_suivantes(x):
        #retourne les cases suivantes possibles à partir de l'abscisse d'une case quelconque
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
		# l'envoye dans la bonne liste, si le chemin est terminé ou non
		#actualise les poids !!!
		chemin_init.append(case)
		global liste_chemins
		global solutions
		global n
		if len(chemin_init) == n:
			solutions.append(chemin_init)
		else :
			liste_chemins.append(chemin_init)
			liste_poids.append(poids(chemin_init))
	
	def nouveauxChemins(x_array):
		#entrée : un chemin (x_array)
		# -> continue / créé de nouveaux x_arrays (avec copieChemin) si nécessaire
		# -> coupe les chemins créés trop grands
		#OUT : tous les chemins valides 
		#type(out) : None
		global a #ame du visiteur
		for i in meilleureCase(x_array):
			if poids(x_array) + plateau[len(x_array)][i] <= a:
				copieChemin(x_array, i)


		
##################  MAIN  ##################################				   
    end = (liste_chemins == [])
 ##################  CONDITIONS MAINLOOP  ##################

	#tant que le plus court chemin n'est pas trop grand (si liste_chemins == []) -----------------------------> OK

 ###########################################################

 	#TODO : boucle qui prend le plus court chemin
    # -> le supprime avec .pop() de liste_chemins
    # -> supprimer aussi le numéro de liste_poids correcpondant
    # -> envoyé à nouveauxChemins
    # si le chemin initial a une longueur de n - 1 :
    # 	|-> .extend() sur solutions
    # sinon : 
    #	|-> .extend() sur liste_chemins des nouveauxChemins() du x_array
    # ...

	while not end:
		for i in meilleurChemin(liste_poids):
			nouveauxChemins(liste_chemins.pop(i))

	if solutions == []:
		stdout.write("IMPOSSIBLE")	
	else :
		

        
labyrinthe_demoniaque()
