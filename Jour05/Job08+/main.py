def my_sort(arr):
    sorted = False  # Variable pour vérifier si la liste est triée
    count = 0  # Compteur du nombre de coups nécessaires pour trier la liste

    while not sorted:
        sorted = True  # Supposons que la liste est triée à chaque itération
        for i in range(len(arr) - 1):
            if arr[i] > arr[i + 1]:  # Vérifie si les éléments adjacents sont dans le bon ordre
                arr[i], arr[i + 1] = arr[i + 1], arr[i]  # Échange les éléments
                sorted = False  # Réinitialise le statut trié car un échange a été effectué
                count += 1  # Incrémente le compteur de coups
    return arr, count  # Retourne la liste triée et le nombre total de coups nécessaires

# Exemple d'utilisation de la fonction
ma_liste = [4, 2, 7, 1, 9, 5]
resultat, coups = my_sort(ma_liste)
print("Liste triée :", resultat)
print("Nombre de coups nécessaires pour trier la liste :", coups)

