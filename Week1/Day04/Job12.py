def tri_liste(liste):
    n = len(liste)
    for i in range(n):
        for j in range(i+1, n):
            if liste[j] < liste[i]:
                liste[i], liste[j] = liste[j], liste[i]
    return liste

L = [7, 11, 42, 39, 2]
print("La liste originale est:", L)

tri_liste(L)
print("La liste triée est:", L)