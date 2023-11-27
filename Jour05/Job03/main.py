def afficher_triangle(hauteur):
    for i in range(hauteur):
        if i == hauteur - 1:
            print('/' + '_' * (2 * i) + '\\')
        else:
            print(' ' * (hauteur - i - 1) + '/' + ' ' * (2 * i) + '\\')

# Demander à l'utilisateur la hauteur du triangle
hauteur = int(input("Entrez la hauteur du triangle : "))

# Affiche le triangle
afficher_triangle(hauteur)

