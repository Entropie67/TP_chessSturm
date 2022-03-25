from vues.menu import Menu
from controleurs.gestion_tournois import GestionTournois

class Start:


    def __init__(self):
        self.menu = Menu()
        self.choix = self.menu.accueil()
        self._routage()


    def _routage(self):
        if self.choix == 1:
            print("... Process...")
            start = GestionTournois(1, self.menu.tournois())
        else:
            print("Choix invalide")
