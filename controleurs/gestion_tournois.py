from modeles.tournois import Tournois
from modeles.ronde import Ronde
from modeles.match import Match


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

        # pour tester
        l = self.make_match()
        for i in l:
            print(i)

    def make_match(self):
        liste_matchs = []
        listes_joueurs = self.tournois.players
        if self.tournois.get_num_ronde() == 0:
            print("lancement du tris")
            # On tris les joueurs en fonction de leurs classement (elo)
            listes_joueurs = sorted(listes_joueurs, key=lambda x: x['joueur'].classement, reverse=True)
            liste_matchs = [Match(listes_joueurs[i], listes_joueurs[i + 4]) for i in range(4)]
            # set une ronde 1 ici + mettre à jour les infors joueurs
        else:
            pass

        return liste_matchs

    def _trier_joueur(self, liste):

        return liste