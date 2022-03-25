from vues.menu import Menu
from controleurs.gestion_tournois import GestionTournois

class Start:


    def __init__(self):
        self.menu = Menu()
        self.choix = self.menu.accueil()
        self._routage()


    def state(self):
        return self.state

    def _routage(self):
        if self.choix == 0:
            self._routage()
        else:
            print("... Process...")
            start = GestionTournois(1)