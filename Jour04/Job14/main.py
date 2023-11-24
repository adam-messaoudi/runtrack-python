def my_long_word(longueur_min, phrase):
    mots = phrase.split()
    mots_filtres = []

    mot_actuel = ''
    for caractere in phrase:
        if caractere != ' ':
            mot_actuel += caractere
        else:
            if len(mot_actuel) > longueur_min:
                mots_filtres.append(mot_actuel)
            mot_actuel = ''

    if len(mot_actuel) > longueur_min:
        mots_filtres.append(mot_actuel)

    return ' '.join(mots_filtres)

resultat = my_long_word(3, "La peur est le chemin vers le côté obscur, la peur mène à la colère, la colère mène à la haine, la haine mène à la souffrance")
print("Output :", resultat)
