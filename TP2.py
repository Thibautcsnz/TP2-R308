import json
import pickle

"""
--------------------------------------
|           Personnage               |
--------------------------------------
| - pseudo: str                     |
| - niveau: int                     |
| - points_de_vie: int              |
| - initiative: int                 |
--------------------------------------
| + Personnage (pseudo: str):
| + Personnage (pseudo:str, n:int): |
| + attaque(assaillant:Personnage): |
| + combat(assaillant:Personnage):  |
| + soigner()                       |
--------------------------------------
"""
#Class Personnage
class personnage:
    def __init__(self, pseudo, niveau=1):
        self.__pseudo = pseudo
        self.__niveau = niveau
        self.__nbvie = niveau
        self.__ini = niveau

    """
        classe personnage:

        cette classe permet de définir un personnage possédant un pseudo, un niveau, un nombre de vies, et un nombre d'initiatives

        .. py:attribute:: pseudo:

            pseudo du personnage

            :type: str

        .. py:attribute:: niveau:

            niveau du personnage

            :type: int

        .. py:attribute:: nbvie

            nombre de vies du personnage

            :type: int

        .. py:attribute:: ini

            nombre d'initiatives du personnage

            :type: int
        """
    """
    @property
    def niveau(self)-> int:
        return self.__niveau
    @niveau.setter
    def niveau(self, niveau:int):
        if is instance(niveau,int):
            if niveau > 0:
                self.__niveau = niveau
    """
    def get_pseudo(self):
        return self.__pseudo
    def get_niveau(self):
        return self.__niveau
    def set_pseudo(self, new_pseudo):
        self.__pseudo = new_pseudo
    def set_niveau(self, new_niveau):
        self.__niveau = new_niveau
    def get_nbvie(self):
        return self.__nbvie
    def get_ini(self):
        return self.__ini
    def set_nbvie(self, new_nbvie):
        self.__nbvie = new_nbvie
    def set_ini(self, new_ini):
        self.__ini = new_ini

    def attaquer(self, assaillant):
        if self.__ini > assaillant.__ini:
            assaillant.__nbvie -= self.__niveau
            if assaillant.__nbvie > 0:
                self.__nbvie -= assaillant.__niveau
        elif self.__ini < assaillant.__ini:
            self.__nbvie -= assaillant.__niveau
            if self.__nbvie > 0:
                assaillant.__nbvie -= self.__niveau
        else:
            self.__nbvie -= assaillant.__niveau
            assaillant.__nbvie -= self.__niveau
    """
    fonction qui permet au personnage d'attaquer

    :param texte: attaque de personnage
    :type texte: str
    :return: le résultat de l'attaque
    :rtype: str
    """
    def combat(self, assaillant):
        while self.__nbvie > 0 and assaillant.__nbvie > 0:
            self.attaquer(assaillant)
    """
        fonction qui permet au personnage d'attaquer

        :param texte: attaque de personnage
        :type texte: str
        :return: le résultat de l'attaque
        :rtype: str
        """
    def soins(self):
        self.__nbvie = self.__niveau

    def degats(self):
        return self.__niveau

    # Programme principal pour tester la classe Personnage
if __name__ == "__main__":
    # Création de deux personnages
    personnage1 = personnage("Thibaut", niveau=5)
    personnage2 = personnage("Mathieu", niveau=3)

    # Affichage des caractéristiques initiales
    print(f"{personnage1.get_pseudo()}: Niveau {personnage1.get_niveau()}, Points de vie {personnage1.get_nbvie()}")
    print(f"{personnage2.get_pseudo()}: Niveau {personnage2.get_niveau()}, Points de vie {personnage2.get_nbvie()}")

    # Combat entre les deux personnages
    personnage1.combat(personnage2)

    # Affichage des caractéristiques après le combat
    print("\nAprès le combat :")
    print(f"{personnage1.get_pseudo()}: Niveau {personnage1.get_niveau()}, Points de vie {personnage1.get_nbvie()}")
    print(f"{personnage2.get_pseudo()}: Niveau {personnage2.get_niveau()}, Points de vie {personnage2.get_nbvie()}")

    # Soigner le premier personnage
    if personnage1.get_nbvie() > 0:
        personnage1.soins()
        print("\nAprès avoir soigné le premier personnage :")
        print(f"{personnage1.get_pseudo()}: Niveau {personnage1.get_niveau()}, Points de vie {personnage1.get_nbvie()}")
    else:
        print(f"{personnage1} est mort ")

    if personnage2.get_nbvie() > 0:
        personnage2.soins()
        print("\nAprès avoir soigné le deuxième personnage :")
        print(f"{personnage2.get_pseudo()}: Niveau {personnage2.get_niveau()}, Points de vie {personnage2.get_nbvie()}")
    else:
        print(f"{personnage2.get_pseudo()} est mort ")

"""
--------------------------------------
|           Guerrier                |
--------------------------------------
|                                   |
--------------------------------------
| + Guerrier (pseudo: str):         |
| + Guerrier (pseudo:str,           |
|               niveau: int)        |
| + degats(): int                   |
| + soin() :                        |          
--------------------------------------
"""
# Classe Guerrier (hérite de Personnage)
class Guerrier(personnage):
    def __init__(self, pseudo, niveau=1):
        # Appel du constructeur de la classe parente (Personnage)
        super().__init__(pseudo, niveau)

        # Calcul des points de vie et de l'initiative spécifiques aux guerriers
        self.__points_de_vie = niveau * 8 + 4
        self.__initiative = niveau * 4 + 6

    def degats(self):
        return self.__niveau * 2
"""
--------------------------------------
|               Mage                |
--------------------------------------
| - mana: int                       |
--------------------------------------
| + Guerrier(ps : String):          |
| + Guerrier(ps : String, niveau    |
|            :int):                 |
| + soin():                         |
| + degats(): int                   |
--------------------------------------
"""
class Mage(personnage):
    def __init__(self, pseudo, niveau=1):
        super().__init__(pseudo, niveau)

        # Calcul des points de vie, de l'initiative et de la mana spécifiques aux mages
        self.__points_de_vie = niveau * 5 + 10
        self.__initiative = niveau * 6 + 4
        self.__mana = niveau * 5

    def get_mana(self):
        return self.__mana

    def set_mana(self, new_mana):
        self.__mana = new_mana

    def degats(self):
        if self.__mana >= 4:
            self.__mana -= 4
            return self.__niveau + 3
        else:
            return self.__niveau

if __name__ == "__main__":
    # Création de personnages
    personnage1 = personnage("Joueur1", niveau=5)
    guerrier1 = Guerrier("Guerrier1", niveau=3)
    mage1 = Mage("Mage1", niveau=4)

    # Combats
    personnage1.combat(guerrier1)
    guerrier1.combat(mage1)
    mage1.combat(personnage1)

# Classe Joueur
"""
--------------------------------------
|               Joueur              |
--------------------------------------
| - nom: String                     |
| - liste_Personnage: Personnage[]  |
| - maximum : int                   |
--------------------------------------
| - Joueur(nom: String):            |
| - Joueur(nom: String,             |
|    maximum: int):                 |
| - Joueur(nom: String, liste_p:    |
|       personnage[]):
| - Joueur(nom: String, liste_p:    |
|       personnage[], maximum: int  |
| + ajouter_Personnage(p:           |
|        personnage):               |
| + rechercher_personnage(id:       |
|   int):personnage                 |
| + rechercher_personnage(p:        |
|    personnage):personnage         |
| + rechercher_personnage(nom:      |
|    string):personnage             |
| + effacer_personnage(id:int):     |
| + effacer_personnage(nom:string): |
| + effacer_personnage(p:personnage):|
--------------------------------------
"""
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

#sérialisation binaire et json à faire

# Créez des instances de vos classes
personnage1 = personnage("Thibaut", niveau=5)
guerrier1 = Guerrier("Guerrier1", niveau=3)
mage1 = Mage("Mage1", niveau=4)

# Sérialisez les objets en binaire
with open("personnages.bin", "wb") as fichier_pickle:
    pickle.dump([personnage1, guerrier1, mage1], fichier_pickle)

# Chargez les objets depuis le fichier binaire
with open("personnages.bin", "rb") as fichier_pickle:
    personnages_charges = pickle.load(fichier_pickle)

# Accédez aux objets désérialisés
personnage1_charge = personnages_charges[0]
guerrier1_charge = personnages_charges[1]
mage1_charge = personnages_charges[2]

# Vous pouvez maintenant utiliser les objets comme d'habitude
print(f"Personnage chargé : {personnage1_charge.get_pseudo()}")

# Créez des instances de vos classes
personnage1 = personnage("Thibaut", niveau=5)
guerrier1 = Guerrier("Guerrier1", niveau=3)
mage1 = Mage("Mage1", niveau=4)

# Convertissez les objets en dictionnaires
personnage1_dict = {
    "pseudo": personnage1.get_pseudo(),
    "niveau": personnage1.get_niveau(),
    "nbvie": personnage1.get_nbvie(),
    "ini": personnage1.get_ini()
}

guerrier1_dict = {
    "pseudo": guerrier1.get_pseudo(),
    "niveau": guerrier1.get_niveau(),
    "nbvie": guerrier1.get_nbvie(),
    "ini": guerrier1.get_ini()
}

mage1_dict = {
    "pseudo": mage1.get_pseudo(),
    "niveau": mage1.get_niveau(),
    "nbvie": mage1.get_nbvie(),
    "ini": mage1.get_ini(),
    "mana": mage1.get_mana()
}

# Créez un dictionnaire global pour stocker vos personnages
personnages_dict = {
    "personnage1": personnage1_dict,
    "guerrier1": guerrier1_dict,
    "mage1": mage1_dict
}

# Sérialisez le dictionnaire en JSON
with open("personnages.json", "w") as fichier_json:
    json.dump(personnages_dict, fichier_json, indent=4)

# Chargez les données depuis le fichier JSON
with open("personnages.json", "r") as fichier_json:
    personnages_charges_dict = json.load(fichier_json)

# Accédez aux données désérialisées pour créer de nouvelles instances de vos classes
personnage1_charge_dict = personnages_charges_dict["personnage1"]
guerrier1_charge_dict = personnages_charges_dict["guerrier1"]
mage1_charge_dict = personnages_charges_dict["mage1"]

# Créez de nouvelles instances de vos classes à partir des dictionnaires
personnage1_charge = personnage(
    personnage1_charge_dict["pseudo"],
    personnage1_charge_dict["niveau"]
)

guerrier1_charge = Guerrier(
    guerrier1_charge_dict["pseudo"],
    guerrier1_charge_dict["niveau"]
)

mage1_charge = Mage(
    mage1_charge_dict["pseudo"],
    mage1_charge_dict["niveau"]
)





