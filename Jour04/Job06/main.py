def echanger_premier_dernier(liste):
    if liste:  
        print(liste)
        liste[0], liste[-1] = liste[-1], liste[0]
        print(liste)

ma_liste = [1, 2, 3, 4, 5]
echanger_premier_dernier(ma_liste)

