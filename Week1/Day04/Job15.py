ma_liste = [22.4, 4.0, 16.22, 9.10, 11.00, 12.22, 14.20, 5.20, 17.50]

liste_arrondie = [round(nombre) for nombre in ma_liste]

liste_triee = sorted(liste_arrondie)

print(liste_triee)