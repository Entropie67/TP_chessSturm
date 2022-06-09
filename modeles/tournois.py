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
        t = {1: "blitz", 2: "bullet", 3: "Un coup rapide"}
        self.temps = t[temps]
        self.description = description
        self.etat_joueur =[]


    def __str__(self):
        return f" \n#### Tournois {self.name} ####\n" \
               f"Lieu: {self.lieu} date : {self.date} \nSystème: {self.temps}" \
               f"Description :{self.description}" \
               f"\nJoueurs : {'---'.join([str(j['joueur']) for j in self.joueurs])}"

    def add_player(self, player):
        self.joueurs.append({"joueur": player, "score": 0, "adversaires": []})

    @property
    def players(self):
        return self.joueurs

    def add_rond(self, liste):
        self.rondes.append(liste)

    def get_num_ronde(self):
        return len(self.rondes)

