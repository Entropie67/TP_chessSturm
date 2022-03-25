from controleurs.gestion_tournois import GestionTournois

class Menu:

    def __init__(self):
        print("#" * 30)
        print("#\tDébut du programme\t\t#")
        print("#" * 30)
        self.choix = 0


    def tournois(self):
        nom = input("Quelle est le nom du tournois ?\t")
        lieu = input("Ou se déroule le tournois ?\t")
        date = input("Quand se déroule le tournois ?\t")
        temps = int(input("1. Blitz 2. Bulet 3. Un coup rapide ?\t"))
        description = input("Entrez une desciption du tournois ?\t")
        return nom, lieu, date, temps, description

    def joueur(self):
        nom = input("Quelle est le nom du joueur ?\t")
        age = int(input("Age du joueur ?\t"))
        sexe = input("Sexe ?\t")
        date = input("Date de naissance ?\t")
        classement = int(input("Classement du joueur ?\t"))
        return nom, age, sexe, date, classement

    def accueil(self):
        print("\nFaites votre choix:")
        print("1. Créer un nouveau tournois")
        print("2. Ajouter des joueurs au tournois")
        print("3. Afficher le tournois")
        print("4. Démarrer le tournois")
        print("5. Sauvegarder le tournois")
        print("6. Reprendre le tournois")
        self.choix = int(input("\n choix : "))
        return self.choix

