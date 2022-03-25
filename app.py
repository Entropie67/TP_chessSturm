from modeles.joueur import Joueur
from controleurs.start import Start

def main():
    # tournois = GestionTournois()
    Start()
    player1 = Joueur("Kasparov", "Gary", "M", "16/02/1975", 3000)
    print(player1)


if __name__ == "__main__":
    main()