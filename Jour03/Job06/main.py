def number_sign(nombre):
    if nombre > 0:
        print("positif")
    elif nombre < 0:
        print("negatif")
    else:
        print("nul")

#Appels de la fonction avec différents paramètres
number_sign(5)
number_sign(-3)
number_sign(0)
