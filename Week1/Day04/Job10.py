L = [8, 24, 27, 48, 2, 16, 9, 102, 7, 84, 91]
produit = 1


for num in L:
    if num >= 25 and num <= 90:
        produit *= num


print("Le produit de toutes les valeurs dans la liste dans l'intervalle [25, 90] est: ", produit)