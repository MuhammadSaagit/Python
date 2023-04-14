import string

def modify_word(word): 
    word = ''.join(char for char in word if char.isalpha()).lower()
    sorted_word = ''.join(sorted(word))
    if sorted_word == string.ascii_lowercase:
        return "Désolé, l'ordre alphabétique maximum a déjà été atteint."
    else:
        for i in range(len(word)):
            if word[i] != sorted_word[i]:
                new_word = word[:i] + sorted_word[i] + ''.join(sorted(word[i+1:]))
                break
        return f"The modified word is: {new_word}"

word = input("Veuillez saisir un mot composé uniquement de lettres :")
print(modify_word(word))