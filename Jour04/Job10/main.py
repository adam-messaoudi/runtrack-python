def produit_intervalle(liste):
    produit = 1
    for nombre in liste:
        if 25 <= nombre <= 90:
            produit *= nombre
    return produit

L = [8, 24, 27, 48, 2, 16, 9, 102, 7, 84, 91]

resultat = produit_intervalle(L)
print(resultat)

