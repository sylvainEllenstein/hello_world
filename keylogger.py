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
    # majs = mins.upper()
    nums = "0123456789"
    nSousChaines = n - k + 1
    nValides = 0
    
    sChaine = chaine[:k]
    wordHashmap = {"nmins" : 0,  "nmajs" : 0, "nnums" : 0, "nspec" : 0}
    
    def typeChar(char) :
        if char in specChar :
            return "nspec"
        if char in mins :
            return "nmins"
        if char in nums : 
            return "nnums"
        return "nmajs"
    
    for char in sChaine :
        wordHashmap[typeChar(char)] += 1
        
    if all([i for i in wordHashmap.values()]) :
        nValides += 1
    
    for i in range(nSousChaines -  1):
        deletedChar = chaine[i] ; addedChar = chaine[i + k]
        wordHashmap[typeChar(deletedChar)] -= 1
        wordHashmap[typeChar(addedChar)] += 1
        
        if all([i for i in wordHashmap.values()]) :
            nValides += 1
        

    return nValides

if __name__ == '__main__':
    n = int(input())
    k = int(input())
    chaine = list(input())
    N = fuite_de_clavier(n, k, chaine)
    print(N)
