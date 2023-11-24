def arrondir_nombres_et_trier(liste):
    for i in range(len(liste)):

        decimale = liste[i] - int(liste[i])
        if decimale >= 0.5:
            liste[i] = int(liste[i]) + 1
        else:
            liste[i] = int(liste[i])

    n = 0
    while n < len(liste) - 1:
        if liste[n] > liste[n + 1]:
            liste[n], liste[n + 1] = liste[n + 1], liste[n]
            n = 0
        else:
            n += 1
    return liste

ma_liste = [22.4, 4.0, 16.22, 9.10, 11.00, 12.22, 14.20, 5.20, 17.50]

resultat = arrondir_nombres_et_trier(ma_liste)
print("Liste arrondie et triée :", resultat)

