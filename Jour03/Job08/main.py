def fruits_legumes(type, saison):
    if type == "fruits" and saison == "hiver":
        print("orange, mandarine et kiwi")
    elif type == "fruits" and saison == "été":
        print("Poire, fraise, cassis")
    elif type == "legume" and saison == "hiver":
        print("carotte, topinambour, endive")
    elif type == "legume" and saison == "été":
        print("artichaut, aubergine, navet")
    else:
        print("Autre fruits/légumes et saison")

#Appel la fonction
fruits_legumes("fruits", "hiver")
fruits_legumes("legume", "hiver")
fruits_legumes("legume", "été")
fruits_legumes("fruits", "été")
fruits_legumes("fruits", "printemps")
