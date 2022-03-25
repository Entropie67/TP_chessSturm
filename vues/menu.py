from controleurs.gestion_tournois import GestionTournois

class Menu:

    def __init__(self):
        print("#" * 30)
        print("#\tDébut du programme\t\t#")
        print("#" * 30)
        self.choix = 0


    def joueur(self):
        pass

    def tournois(self):
        nom = input("Quelle est le nom du tournois ?\t")
        lieu = input("Ou se déroule le tournois ?\t")
        date = input("Quand se déroule le tournois ?\t")
        temps = input("1. Blitz 2. Bulet 3. Un coup rapide ?\t")
        description = input("Entrez une desciption du tournois ?\t")
        return nom, lieu, date, temps, description

    def accueil(self):
        print("\nFaites votre choix:")
        print("1. Créer un nouveau tournois")
        self.choix = int(input("\n choix : "))
        return self.choix

