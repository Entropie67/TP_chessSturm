from modeles.tournois import Tournois


class GestionTournois:
    """
        Classe gérant le tournois
    """

    def __init__(self, choix, state=None):
        self.tournois = None
        self.data = state
        if choix == 1:
            self.creat()
        else:
            print("On fait autre chose avec un tournois")

    def creat(self):

        self.tournois = Tournois(*self.data)
        print(self.tournois)

    def edit(self):
        pass

    def save(self):
        pass

    