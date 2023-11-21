def contient_e(chaine):
    if 'e' in chaine:
        return True
    else:
        return False

mot = input("Entrez une chaîne de caractères : ")
if contient_e(mot):
    print("La chaîne contient le caractère 'e'.")
else:
    print("La chaîne ne contient pas le caractère 'e'.")
