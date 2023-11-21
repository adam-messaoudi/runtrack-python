chaine = "abcdefghijklmnopqrstuvwxyz" * 10
longueur_chaine = len(chaine)
ligne = 1
caractere_actuel = 0

while caractere_actuel < longueur_chaine:
    print(chaine[caractere_actuel:caractere_actuel + ligne])
    caractere_actuel += ligne
    ligne += 1
