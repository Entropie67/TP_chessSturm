from modeles.tournois import Tournois


class GestionTournois:
    """
        Classe gérant le tournois
    """

    def __init__(self):
        self.tournois = None
        self.creat()

    def creat(self):
        self.tournois = Tournois("Tounois des géants", "Strasbourg", "01/04/2002")
        print(self.tournois)

    def edit(self):
        pass

    def save(self):
        pass

    