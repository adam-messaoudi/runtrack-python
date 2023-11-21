
montant_initial = 10000
taux_rendement_annuel = 5


gain_annuel = (montant_initial * taux_rendement_annuel) / 100
print(f"Gain annuel : {gain_annuel} euros")

montant_initial += 5000
taux_rendement_annuel += 2

nouveau_gain_annuel = (montant_initial * taux_rendement_annuel) / 100
print(f"Nouveau gain annuel : {nouveau_gain_annuel} euros")


montant_initial -= montant_initial * 0.10
taux_rendement_annuel -= 1

51
montant_final = montant_initial + nouveau_gain_annuel
print(f"Montant final de l'investissement : {montant_final} euros")
