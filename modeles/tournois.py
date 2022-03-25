class Tournois:
    """
        Classe qui modélise un tournois
    """

    def __init__(self, nom, lieu, date, temps, description, nb_tour=4):
        self.name = nom
        self.lieu = lieu
        self.date = date
        self.nb_tour = nb_tour
        self.rondes = []
        self.joueurs = []
        t = ["blitz", "bullet", "Un coup rapide"]
        self.temps = t[temps + 1]
        self.description = description

    def __str__(self):
        return f" \n#### Tournois {self.name} ####\n" \
               f"Lieu: {self.lieu} date : {self.date} \nSystème: {self.temps}" \
               f"Description :{self.description}" \
               f"\nJoueurs : {'---'.join([str(j) for j in self.joueurs])}"

    def add_player(self, player):
        self.joueurs.append(player)