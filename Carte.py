class Carte:
    valeurs = (None, None, 2, 3, 4, 5, 6, 7, 8, 9, 10, "Valet", "Dame", "Roi", "As")
    couleurs = ("Coeur", "Carreau", "Trèfle", "Pique")

    def __init__(self, val, coul):
        if val < 2 or val > 14:
            print("Erreur : la valeur d'une carte est comprise entre 2 et 4")
            exit(1)
        if coul < 0 or coul > 3:
            print("Erreur : le code couleur d'une carte est compris entre 0 et 3")
            exit(1)
        self.__valeur = val
        self.couleur = coul


    def affiche(self):
        print(Carte.valeurs[self.valeur], "de", Carte.couleurs[self.couleur])

    def affiche_ascii(self):
        nom = str(Carte.valeurs[self.valeur]) + " de " + Carte.couleurs[self.couleur]
        taille = len(nom) + 2
        print("/", "-" * taille, "\\", sep="")
        print("|", " " * taille, "|", sep="")
        print("|", nom, "|")
        print("|", " " * taille, "|", sep="")
        print("\\", "-" * taille, "/", sep="")


    def __str__(self):
        return str(Carte.valeurs[self.valeur]) + " de " + Carte.couleurs[self.couleur]

    def getValeur(self):
        return self.__valeur

    def setValeur(self, val):
        self.__valeur = val