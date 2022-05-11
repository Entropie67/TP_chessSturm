from modeles.tournois import Tournois
from modeles.ronde import Ronde

class GestionTournois:
    """
        Classe gérant le tournois
    """

    def __init__(self):
        self.tournois = None
        self.data = None

    def creat(self, data):
        self.tournois = Tournois(*data)

    def edit(self):
        pass

    def save(self):
        pass

    def display(self):
        print(self.tournois)

    def add_players(self, joueur):
        self.tournois.add_player(joueur)

    def start_play(self):
        pass

    def make_match(self):
        listes_joueurs = self.tournois.get_players()

    def _trier_joueur(self):
        pass