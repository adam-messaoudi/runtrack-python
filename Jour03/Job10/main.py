def pair_impair(nombre):
    if isinstance(nombre, int) and nombre >= 0:
        if nombre % 2 == 0:
            print("Pair")
        else:
            print("Impair")
    else:
        print("Nombre non valide")

# Appels de la fonction avec différents paramètres
pair_impair(5)
pair_impair(10)
pair_impair(-3)
pair_impair(7)
