from typing import any



class Joueur:

    """
        Cette classe permet de modéliser un joueur
    """

    def __init__(self, name: str, age: int, sexe: str, date: str, elo: int) -> None:
            self.name = name
            self.age = age
            self.sexe = sexe
            self.date_naissance = date
            self.elo = elo

    def __str__(self) -> str:
        return f"\nNom: {self.name},\nAge: {self.age},\nSexe: {self.sexe}," \
               f"\nDate de naissance :{self.date_naissance},\nClassement: {self.elo}\n"

    @property
    def classement(self) -> int:
        return self.elo

    @classement.setter
    def classement(self, val: int) -> None:
        self.elo = val

    def __eq__(self, other) -> bool:
        """ Méthode spéciale pour tester l'égalité de classement de deux joueurs"""
        if self.elo == other.classement:
            return True
        else:
            return False

    def __lt__(self, other) -> bool:
        if self.elo < other.classement:
            return True
        else:
            return False

    def __gt__(self, other) -> bool:
        if self.elo > other.classement:
            return True
        else:
            return False

