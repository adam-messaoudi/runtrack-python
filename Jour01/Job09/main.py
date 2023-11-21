
nom_produit = "Ordinateur"
prix_unitaire = 1000
quantite_stock = 50

print(f"Nom du produit : {nom_produit}")
print(f"Prix unitaire : {prix_unitaire} euros")
print(f"Quantité en stock : {quantite_stock}")


achat = int(input("Combien de produits souhaitez-vous acheter ? "))
quantite_stock += achat

prix_unitaire *= 1.10  

print("\nInformations mises à jour sur le produit :")
print(f"Nom du produit : {nom_produit}")
print(f"Nouveau prix unitaire : {prix_unitaire} euros")
print(f"Nouvelle quantité en stock : {quantite_stock}")
