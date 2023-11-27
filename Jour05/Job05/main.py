def chiffrement_cesar(message, decalage):
    message_chiffre = ''  # Initialise une chaîne vide pour stocker le message chiffré
    for lettre in message:  # Parcourt chaque caractère du message
        if lettre.islower():  # Vérifie si la lettre est en minuscule
            # Effectue le décalage pour la lettre en minuscule
            lettre_decalee = chr(((ord(lettre) - ord('a') + decalage) % 26) + ord('a'))
            message_chiffre += lettre_decalee  # Ajoute la lettre chiffrée à la chaîne de message chiffré
        elif lettre.isalpha():  # Si la lettre est une lettre mais pas en minuscule
            lettre = lettre.lower()  # Convertit la lettre en minuscule
            # Effectue le décalage pour la lettre en minuscule (comme expliqué ci-dessus)
            lettre_decalee = chr(((ord(lettre) - ord('a') + decalage) % 26) + ord('a'))
            message_chiffre += lettre_decalee.upper()  # Ajoute la lettre chiffrée en majuscule à la chaîne de message chiffré
        else:
            message_chiffre += lettre  # Si ce n'est pas une lettre, ajoute le caractère tel quel au message chiffré

    return message_chiffre  # Renvoie le message chiffré

# Exemple d'utilisation avec un message et un décalage de 3
message_original = "Bonjour, voici un exemple de chiffrement Cesar !"
decalage = 3
message_chiffre = chiffrement_cesar(message_original, decalage)  # Appel de la fonction pour chiffrer le message
print("Message original :", message_original)  # Affiche le message original
print("Message chiffré  :", message_chiffre)  # Affiche le message chiffré

