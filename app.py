from modeles.joueur import Joueur
from vues.menu import Menu

def main():
    # tournois = GestionTournois()
    go = Menu()
    player1 = Joueur("Kasparov", "Gary", "M", "16/02/1975", 3000)
    print(player1)


if __name__ == "__main__":
    main()