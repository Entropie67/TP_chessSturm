from controleurs.tournois import GestionTournois

class Menu:

    def __init__(self):
        print("#" * 30)
        print("#\tDébut du programme\t\t#")
        print("#" * 30)
        self.choix = 0
        self._accueil()
        self._routage()

    def _accueil(self):
        print("\nFaites votre choix:")
        print("1. Créer un nouveau tournois")
        self.choix = int(input("\n choix : __"))

    def _routage(self):
        if self.choix == 0:
            self._routage()
        else:
            print("... Process...")
            start = GestionTournois()
