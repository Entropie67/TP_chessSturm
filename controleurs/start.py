from vues.menu import Menu
from controleurs.gestion_tournois import GestionTournois
from modeles.joueur import Joueur


class Start:


    def __init__(self):
        self.menu = Menu()
        self.start = GestionTournois()
        self.choix = -1
        while self.choix != 0:
            self.choix = self.menu.accueil()
            self._routage()


    def _routage(self):
        NB_JOUEURS = 2
        if self.choix == 1:
            print("... Process...")
            self.start.creat(self.menu.tournois())
        elif self.choix == 2:
            for i in range(NB_JOUEURS):
                print(f"\nAjout du joueur numéro {i+1} :\n")
                self.start.add_players(Joueur(*self.menu.joueur()))
        elif self.choix == 3:
            self.start.display()
        elif self.choix == 4:
            pass
        elif self.choix == 5:
            pass
        elif self.choix == 6:
            pass
        else:
            print(" # Choix invalide # ")
