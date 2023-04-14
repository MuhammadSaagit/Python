def display_items(type, season):
    if type == "fruits" and season == "hiver":
        print("orange, mandarine et kiwi")
    elif type == "fruits" and season == "ete":
        print("poire, fraise, cassis")
    elif type == "legume" and season == "hiver":
        print("carotte, topinambour, endive")
    elif type == "legume" and season == "ete":
        print("artichaut, aubergine, navet")
    else:
        print("Error: invalid type or season input")

display_items("fruits", "hiver") # Output: "orange, mandarine et kiwi"
display_items("fruits", "ete") # Output: "poire, fraise, cassis"
display_items("legume", "hiver") # Output: "carotte, topinambour, endive"
display_items("legume", "ete") # Output: "artichaut, aubergine, navet"
display_items("invalid", "invalid") # Output: "Error: invalid type or season input"
