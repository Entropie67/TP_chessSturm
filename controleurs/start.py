from vues.menu import Menu
from controleurs.gestion_tournois import GestionTournois

class Start:


    def __init__(self):
        self.menu = Menu()
        self.choix = self.menu.accueil()
        self.start = GestionTournois()
        self._routage()


    def _routage(self):
        if self.choix == 1:
            print("... Process...")
            self.start.creat(self.menu.tournois())
        elif self.choix == 2:
            start
        else:
            print("Choix invalide")
