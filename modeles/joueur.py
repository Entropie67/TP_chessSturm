

class Joueur:

    """
        Cette classe permet de modéliser un joueur
    """

    def __init__(self, name, age, sexe, date, elo):
            self.name = name
            self.age = age
            self.sexe = sexe
            self.date_naissance = date
            self.elo = elo

    def __str__(self):
        return f"\nNom: {self.name},\nAge: {self.age},\nSexe: {self.sexe}," \
               f"\nDate de naissance :{self.date_naissance},\nClassement: {self.elo}\n"

    @property
    def classement(self):
        return self.elo

    @classement.setter
    def classement(self, val):
        self.elo = val

    def __eq__(self, other):
        if self.elo == other.elo:
            return True
        else:
            return False

    def __lt__(self, other):
        if self.elo < other.elo:
            return True
        else:
            return False

    def __gt__(self, other):
        if self.elo > other.elo:
            return True
        else:
            return False

