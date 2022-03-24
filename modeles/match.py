class Match:
    """
        Classe qui modélise un match
    """

    def __init__(self, joueur_a, joueur_b):
        self.player1 = joueur_a
        self.player2 = joueur_b
        self.resultat = ""

    def __str__(self):
        return f" \n {self.player1} vs. {self.player2} => Résultat {self.resultat}"