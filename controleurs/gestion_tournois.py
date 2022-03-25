from modeles.tournois import Tournois


class GestionTournois:
    """
        Classe gérant le tournois
    """

    def __init__(self, choix):
        self.tournois = None
        if choix == 1:
            self.creat()
        else:
            print("On fait autre chose avec un tournois")

    def creat(self):

        name = input("Quel est le nom du tournois")
        self.tournois = Tournois("Tounois des géants", "Strasbourg", "01/04/2002", 1, "")
        print(self.tournois)

    def edit(self):
        pass

    def save(self):
        pass

    