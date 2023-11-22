def moyenne(note1, note2, note3):
    moyenne_etudiant = (note1 + note2 + note3) / 3
    return moyenne_etudiant

note1 = float(input("Entrez la première note : "))
note2 = float(input("Entrez la deuxième note : "))
note3 = float(input("Entrez la troisième note : "))

resultat_moyenne = moyenne(note1, note2, note3)

if 15 <= resultat_moyenne <= 20:
    print("Très bon élève")
elif 11 <= resultat_moyenne <= 14:
    print("Bon élève")
elif 8 <= resultat_moyenne <= 10:
    print("Élève moyen")
elif 0 <= resultat_moyenne <= 7:
    print("Élève devant faire des efforts")
