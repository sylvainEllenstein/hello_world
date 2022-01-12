
def fuite_de_clavier(n, k, chaine):
    """
    :param n: taille de la chaîne
    :type n: int
    :param k: taille du mot de passe
    :type k: int
    :param chaine: la chaîne contenant le mot de passe
    :type chaine: list[str]
    """
    # TODO afficher le nombre de mots de passes possibles parmi la chaîne
    
    specChar = '"!' + "#$%&'()*+,-./:;<=>?@[\]^_`{|}~"
    mins = "abcdefghijklmnopqrstuvwxyz"
    majs = mins.upper()
    nums = "0123456789"
    nSousChaines = n - k + 1
    nValides = 0
    
    sChaine = chaine[:k]
    wordHashmap = {nmins : 0,  nmajs : 0, nnums : 0, nspec : 0}
    for i in range(1, nSousChaines):
        deletedChar = chaine[i - 1] ; addedChar = chaine[]
        
        # etc ... trier et regarder le type du caractère ajouté / retiré
        
        

    return nValides

if __name__ == '__main__':
    n = int(input())
    k = int(input())
    chaine = list(input())
    N = fuite_de_clavier(n, k, chaine)
