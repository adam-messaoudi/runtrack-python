def distance_toilettes_par_semaine(nombre_marches, hauteur_marche):
    # Calcul de la distance totale parcourue pour un aller-retour aux toilettes
    distance_aller_retour = nombre_marches * hauteur_marche * 2  # Pour monter et descendre

    # Calcul de la distance parcourue par jour pour aller aux toilettes
    distance_par_jour = distance_aller_retour * 5  # Le gardien y va 5 fois par jour

    # Calcul de la distance parcourue par semaine
    distance_semaine = distance_par_jour * 7  # Une semaine comporte 7 jours

    # Conversion en mètres
    distance_semaine_en_metres = distance_semaine / 100  # Convertit les centimètres en mètres

    # Affichage du résultat
    print(f"Pour {nombre_marches} marches de {hauteur_marche} cm, le gardien parcourt {distance_semaine_en_metres:.2f} m par semaine.")

# Exemple d'utilisation de la fonction avec 100 marches de 20 cm chacune
nombre_marches = 100
hauteur_marche = 20
distance_toilettes_par_semaine(nombre_marches, hauteur_marche)
