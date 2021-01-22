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
	
############ RECURSIF #############
    
        
labyrinthe_demoniaque()
