def inverser_premier_et_dernier(donnees):
    if not donnees:
        return donnees
    
    premier_element = donnees[0]
    dernier_element = donnees[-1]
    
    donnees[0] = dernier_element
    donnees[-1] = premier_element
    
    return donnees
# une example
ma_liste = [1, 2, 3, 4, 5]
print(inverser_premier_et_dernier(ma_liste))