def arrondir_notes(notes):
    notes_arrondies = []
    for note in notes:
        if note < 40 or note % 5 == 0:  # Si la note est en dessous de 40 ou déjà multiple de 5, pas d'arrondi
            notes_arrondies.append(note)
        else:
            multiple_5_superieur = ((note + 4) // 5) * 5
            # Vérifie si la note arrondie est supérieure ou égale à 40 et si la différence est inférieure à 3
            if multiple_5_superieur >= 40 and multiple_5_superieur - note < 3:
                notes_arrondies.append(multiple_5_superieur)
            else:
                notes_arrondies.append(note)

    return notes_arrondies

# Exemple d'utilisation de la fonction avec une liste de notes
liste_notes = [83, 72, 57, 40, 38, 91, 98]
notes_arrondies = arrondir_notes(liste_notes)
print("Notes originales    :", liste_notes)
print("Notes arrondies     :", notes_arrondies)



