def time_to_text(minutes):
    heures = minutes // 60
    minutes_restantes = minutes % 60
    print(f"{heures} heures et {minutes_restantes} minutes")

# Appels de la fonction avec différents paramètres
time_to_text(90)
time_to_text(150)
time_to_text(30)
time_to_text(77)
time_to_text(430)
