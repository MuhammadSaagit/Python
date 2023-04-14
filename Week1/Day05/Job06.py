def arrondir_notes(liste_notes):
    notes_arrondies = []
    for note in liste_notes:
        multiple_de_cinq_sup = ((note // 5) + 1) * 5
        if multiple_de_cinq_sup - note < 3 and note >= 38:
            notes_arrondies.append(multiple_de_cinq_sup)
        else:
            notes_arrondies.append(note)
    return notes_arrondies

liste_notes = [5, 9, 11, 12, 14, 16, 17, 37, 42, 45, 48, 53, 57, 61, 64, 69, 74, 78, 85, 88, 92, 97]
notes_arrondies = arrondir_notes(liste_notes)
print(notes_arrondies) 