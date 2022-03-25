from modeles.tournois import Tournois


class GestionTournois:
    """
        Classe gérant le tournois
    """

    def __init__(self):
        self.tournois = None
        self.data = None


    def creat(self, data):

        self.tournois = Tournois(*data)
        print(self.tournois)

    def edit(self):
        pass

    def save(self):
        pass


    def add_players(self, joueur):

        self.tournois.add_player(joueur)

    