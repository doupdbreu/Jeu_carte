from JeuCarte import JeuCarte

if __name__ == "__main__":
    j = JeuCarte()
    print(j)
    j.melanger()
    print(j)

    carte = j.tirer()
    print(carte)


