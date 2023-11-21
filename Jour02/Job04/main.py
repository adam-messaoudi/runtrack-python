while True:
    try:
        N = int(input("Entrez un entier supérieur à zéro : "))
        if N <= 0:
            raise ValueError("Veuillez entrer un entier supérieur à zéro.")
        break
    except ValueError as e:
        print(e)

for i in range(1, N + 1):
    print(f"Table de multiplication pour {i} :")
    for j in range(1, 11):
        print(f"{i} * {j} = {i * j}")
    print()
