from controleurs.gestion_tournois import GestionTournois

class Menu:

    def __init__(self):
        print("#" * 30)
        print("#\tDébut du programme\t\t#")
        print("#" * 30)
        self.choix = 0


    def tournois(self, test=False):
        if test:
            nom = "Tournois de Strasbourg"
            lieu = "Strasbourg"
            date = "02/02/2023"
            temps = 1
            description = "Ceci est le tournois de test, généré automatiquement."
        else:
            nom = input("Quelle est le nom du tournois ?\t")
            lieu = input("Ou se déroule le tournois ?\t")
            date = input("Quand se déroule le tournois ?\t")
            temps = int(input("1. Blitz 2. Bulet 3. Un coup rapide ?\t"))
            description = input("Entrez une desciption du tournois ?\t")
        return nom, lieu, date, temps, description

    def joueur(self, test=False):
        if test: # Achanger pour un ajout automatique des joueurs
            import random
            from faker import Factory
            fake = Factory.create('fr_FR')
            s = ["F", "M"]
            nom = fake.name()
            age = random.randint(11, 93)
            sexe = s[random.randint(0, 1)]
            date = "21/09/2005"
            classement = random.randint(1000, 3000)
        else:
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
        print("7. Mode test avec joueurs et tournois automatiques")
        self.choix = int(input("\n choix : "))
        return self.choix

