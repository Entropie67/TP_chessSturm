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
               f"Lieu: {self.lieu} date : {self.date} Système: {self.temps}" \
               f"Description :{self.description}" \
               f"Joueurs : {[print(j) for j in self.joueurs]}"

    def add_player(self, player):
        self.joueurs.append(player)