
def resoudre(ncouleurs, couleurs, ncotes, couleurscotes, npieces, pieces):
    """
    :param ncouleurs: le nombre de couleurs
    :type ncouleurs: int
    :param couleurs: les différentes couleurs possibles
    :type couleurs: list[str]
    :param ncotes: le nombre de côtés de la pièce manquante
    :type ncotes: int
    :param couleurscotes: les couleurs des pièces adjacentes à la pièce manquante
    :type couleurscotes: list[str]
    :param npieces: le nombre de pièces à trier
    :type npieces: int
    :param pieces: les pièces à trier
    :type pieces: list[dict["nCotesPiece": int, "couleurPiece": str]]
    """
    # TODO Affiche sur la première ligne, pour chaque pièce un caractère 'O' si
    # la pièce peut correspondre à celle recherchée, 'X' sinon. Affiche sur la
    # ligne suivante le nombre de pièces qui peuvent correspondre.
    pass


if __name__ == '__main__':
    ncouleurs = int(input())
    couleurs = [input() for _ in range(ncouleurs)]
    ncotes = int(input())
    couleurscotes = [input() for _ in range(ncotes)]
    npieces = int(input())
    pieces = [{
        "nCotesPiece": int(input()),
        "couleurPiece": input()
    } for _ in range(npieces)]
    resoudre(ncouleurs, couleurs, ncotes, couleurscotes, npieces, pieces)
