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

    a = int(input())
    n = int(input()) #longueur
    m = int(input()) #largeur
    plateau = [list(map(int, input().split(" "))) for _ in range(n)]
    tous_chemins = [] for _ in range (0, m)
    
    def cases_suivante(x, largeur):
        #retourne les cases suivantes d'un objet chemin 
        if x == 0: return [0, 1]
        elif x == largeur - 1: return [largeur - 1, largeur]
        return [x - 1, x, x + 1]
    
    def meilleurChemin(tous_chemins):
        #donne le(s) meilleur(s) chemin(s) actuel(s) dans tous les objets chemin
        #entrée : tous_chemins, qui contient tous les objets chemin
        #sortie : [place des chemins dans tou_chemins]
        pass
    
    class chemin:
        def __init__(self, c):
            self.cases = c
            self.poids = sum(c)
            
        def copier(self, nouvelle_case):
        #copie le chemin self et créé un nouveau avec le nouvelle_case en plus
            ch_ = chemin(self.cases)
            pass
        def meilleureCase(liste):
        #calcule la prochaine meilleure case d'un objet chemin
        #A améliorer : doit pouvoir prendre en compte si deux cases ont le même poids -> création d'un nouveau chemin
        pass
        
        def nouvelleCase(self, case):
    
    def main(chemins_possibles, plateau):
        #création de tous les premiers chemins :
        for i in range(0, m):
            tous_chemins[i] = chemin(i)
        
        
        #TODO : boucle qui prend le plus court objet chemin, le continue et actualise sa longueur
        #la boucle coupe si le plus court chemin est plus grand que l'âme du visiteur, et coupe les chemins déjà trop grands
        
        pass
    
        
labyrinthe_demoniaque()
