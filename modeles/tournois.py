class Tournois:
    """
        Classe qui modélise un tournois
    """

    def __init__(self, nom, lieu, date, nb_tour=4):
        self.name = nom
        self.lieu = lieu
        self.date = date
        self.nb_tour = nb_tour
        self.rondes = []
        self.joueurs = []
        self.temps = ""
        self.description = ""

    def __str__(self):
        return f" \n#### Tournois {self.nom} ####\n" \
               f"" \
               f"" \
               f"" \
               f"" \
               f"" \
               f"" \
               f"" \
               f""

    def add_player(self, player):
        self.joueurs.append(player)