from Carte import Carte
import random

class JeuCarte:
    def __init__(self):
        self.cartes = []

        for val in range(2, 15):
            for coul in range(4):
                self.cartes.append(Carte(val, coul))

    def __str__(self):
        cartes_du_jeu = ""

        for carte in self.cartes:
            if cartes_du_jeu == "":
                cartes_du_jeu = str(carte)
            else:
                cartes_du_jeu += ", " + str(carte)
        return cartes_du_jeu

    def melanger(self):
        random.shuffle(self.cartes)

    def tirer(self):
        try:
            return self.cartes.pop(0)
        except IndexError as erreur:
            print("Il n'y a plus de carte dans le jeu !")
            return None

