def time_to_text(minutes):
    heures = minutes // 60
    minutes_restantes = minutes % 60
    print(f"{heures} heures et {minutes_restantes} minutes")

# Appel de la fonction 
time_to_text(90)
time_to_text(150)
time_to_text(30)
time_to_text(62)
