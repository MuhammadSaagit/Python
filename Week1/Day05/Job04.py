def shift_alphabet(message, shift):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    shift_alphabet = 'bcedfghijklmnopqrstuvwxyza'
    shifted_message = ''
    for letter in message: 
        if letter.isalpha():
            position = ord(letter) - ord('a')
            new_position = (position + shift) % 26
            shifted_message += chr(new_position + ord('a'))
        else:
            shifted_message += letter
    return shifted_message

message = 'ceasarsalad'
shift = 1
shifted_message = shift_alphabet(message, shift)
print(shifted_message)