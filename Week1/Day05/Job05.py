def calculer_distance(steps, hauteur):
    distance_par_pas = hauteur / 100
    distance_par_jour = (steps * 2 * distance_par_pas) + (100 * distance_par_pas)
    distance_par_semaine = 7 * distance_par_jour
    return f"Pour {steps} pas de {hauteur}cm, le gardien parcourt {distance_par_semaine:.2f}m par semaine"

# Exemple d'utilisation
pas = 50
hauteur = 20
resultat = calculer_distance(pas, hauteur)
print(resultat) # Pour 50 pas de 20cm, le gardien parcourt 210.00m par semaine