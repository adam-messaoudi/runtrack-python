def pair_impair(nombre):
    if isinstance(nombre, int) and nombre >= 0:
        if nombre % 2 == 0:
            print("Pair")
        else:
            print("Impair")
    else:
        print("Nombre non valide")

# Appel de la fonction 
pair_impair(5)
pair_impair(10)
pair_impair(-3)
pair_impair(7.5)
