# Classe Joueur
class Joueur:
    def __init__(self, nom, nombre_max_personnages):
        self.nom = nom
        self.nombre_max_personnages = nombre_max_personnages
        self.personnages = []

    def ajouter_personnage(self, personnage):
        if len(self.personnages) < self.nombre_max_personnages:
            self.personnages.append(personnage)
            print(f"{personnage.get_pseudo()} a été ajouté à la liste des personnages de {self.nom}.")
        else:
            print(f"Impossible d'ajouter {personnage.get_pseudo()}, la limite de personnages est atteinte.")

    def get_personnage_par_numero(self, numero):
        if 0 <= numero < len(self.personnages):
            return self.personnages[numero]
        else:
            print("Numéro de personnage invalide.")
            return None

    def get_personnage_par_pseudo(self, pseudo):
        for personnage in self.personnages:
            if personnage.get_pseudo() == pseudo:
                return personnage
        print(f"Personnage avec le pseudo '{pseudo}' introuvable.")
        return None

    def get_personnage(self, personnage):
        if personnage in self.personnages:
            return personnage
        print("Personnage introuvable.")
        return None

    def eliminer_personnage_par_numero(self, numero):
        if 0 <= numero < len(self.personnages):
            personnage_elimine = self.personnages.pop(numero)
            print(f"{personnage_elimine.get_pseudo()} a été éliminé de la liste des personnages de {self.nom}.")
        else:
            print("Numéro de personnage invalide.")

    def eliminer_personnage_par_pseudo(self, pseudo):
        for personnage in self.personnages:
            if personnage.get_pseudo() == pseudo:
                self.personnages.remove(personnage)
                print(f"{pseudo} a été éliminé de la liste des personnages de {self.nom}.")
                return
        print(f"Personnage avec le pseudo '{pseudo}' introuvable.")

    def eliminer_personnage(self, personnage):
        if personnage in self.personnages:
            self.personnages.remove(personnage)
            print(f"{personnage.get_pseudo()} a été éliminé de la liste des personnages de {self.nom}.")
        else:
            print("Personnage introuvable.")

# Programme principal pour tester la classe Joueur
if __name__ == "__main__":
    joueur1 = Joueur("Joueur1", 3)

    personnage1 = personnage("Perso1", niveau=5)
    personnage2 = personnage("Perso2", niveau=3)
    personnage3 = personnage("Perso3", niveau=4)

    joueur1.ajouter_personnage(personnage1)
    joueur1.ajouter_personnage(personnage2)
    joueur1.ajouter_personnage(personnage3)

    personnage4 = personnage("Perso4", niveau=2)
    joueur1.ajouter_personnage(personnage4)  # Cela atteindra la limite

    print(f"Personnage par numéro: {joueur1.get_personnage_par_numero(1).get_pseudo()}")
    print(f"Personnage par pseudo: {joueur1.get_personnage_par_pseudo('Perso2').get_pseudo()}")
    print(f"Personnage par objet: {joueur1.get_personnage(personnage3).get_pseudo()}")

    joueur1.eliminer_personnage_par_numero(0)
    joueur1.eliminer_personnage_par_pseudo("Perso2")
    joueur1.eliminer_personnage(personnage4)

