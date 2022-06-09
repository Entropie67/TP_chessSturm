from random import randint


class Match:
    """
        Classe qui modélise un match
    """

    def __init__(self, joueur_a, joueur_b):
        self.player_blanc = joueur_a
        self.player_noir = joueur_b
        self._resultat = self._deroulement()

    def __str__(self):
        return f" \n {self.player_blanc['joueur'].name} avec les blanc vs. {self.player_noir['joueur'].name} avec les noirs" \
               f" => Résultat: {self.resultat}"

    def _deroulement(self):
        """
            déroulent automatique du match avec pondération en fonctione l'elo
            0 pour un match nul, 1 pour une victoire des blancs et 2 pour une victoire des noirs
        """
        # Pondération à ajouter
        # resul = int(input("Entrez le résultat du match : "))
        resul = randint(0, 2)
        if resul == 0 :
            self.player_blanc["score"] += 0.5
            self.player_noir["score"] += 0.5
            self.player_blanc["adversaires"].append(self.player_noir['joueur'])
            self.player_noir["adversaires"].append(self.player_blanc['joueur'])
        return resul

    @property
    def resultat(self):
        return self._resultat

    @resultat.setter
    def resultat(self, val):
        self._resultat = val