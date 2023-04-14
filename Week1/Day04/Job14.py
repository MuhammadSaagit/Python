def my_long_word(n, sentence):
    words = sentence.split()
    long_words = [word for word in words if len(word) > n]
    return ' '.join(long_words)

sentence = "La peur est le chemin vers le cote obscur la peur mene á la colere la colere mene a la haine la haine mene a la souffrance"
long_words = my_long_word(3, sentence)
print(long_words)