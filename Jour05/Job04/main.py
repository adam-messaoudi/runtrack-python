def afficher_tapis_diagonale(taille):
    print('+' + '-' * taille + '+')
    for i in range(taille):
        print('|', end='')
        for j in range(taille):
            if i + j != taille - 1:  # Ajouter '#' sauf pour la diagonale de haut à droite vers bas à gauche
                print('#', end='')
            else:
                print(' ', end='')  # Ajouter un espace pour la diagonale
        print('|')
    print('+' + '-' * taille + '+')

# Demander à l'utilisateur la taille du tapis
taille = int(input("Entrez la taille du tapis : "))

# Affiche le tapis
afficher_tapis_diagonale(taille)



