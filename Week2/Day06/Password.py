import hashlib
import json
import random
import string
import re

passwords = []

def add_password_to_file(hashed_password, potato):
    with open('passwords.json', 'r') as f:
        passwords = json.load(f)
    if hashed_password not in passwords.values():
        index = len(passwords) + 1
        passwords[index] = {'password': hashed_password, 'potato': potato}
        with open('passwords.json', 'w') as f:
            json.dump(passwords, f)

def display_passwords():
    with open('passwords.json', 'r') as f:
        passwords = json.load(f)
    if not passwords:
        print("Aucun mot de passe enregistré.")
    else:
        latest_password = max(passwords, key=int)
        print(f"Le mot de passe haché est : {passwords[latest_password]['potato']}")

def validate_password(password):
    if not re.search(r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[!@#$%^&*?', password):
        return False
    else:
        return True
option = ''

while option != '3':
    print('Veuillez sélectionner une option:')
    print('1. ajouter un nouveau mot de passe')
    print('2. Afficher les mots de passe enregistrés')
    print('3. Quitter')
    option = input('Entrez votre choix: ')

    if option == '1':
        while True:
            new_password = input('Entrez le nouveau mot de passe: ')
            if len(new_password) < 8:
                print('Erreur : le mot de passe doit comporter au moins 8 caractères')
            elif not re.search(r'[a-z]', new_password):
                print('Erreur : le mot de passe doit comporter au moins une lettre minuscule')
            elif not re.search(r'[A-Z]', new_password):
                print('Erreur : le mot de passe doit comprendre au moins une lettre majuscule')
            elif not re.search(r'\d', new_password):
                print('Erreur : le mot de passe doit comprendre au moins un chiffre')
            elif not re.search(r'[!@#$%^&*?]', new_password):
                print('Erreur : le mot de passe doit comprendre au moins un caractère spécial')
            else:
                potato = ''.join(random.choices(string.ascii_letters + string.digits, k=16))
                hashed_password = hashlib.sha256((new_password + potato).encode()).hexdigest()
                add_password_to_file(hashed_password, potato)
                print('Mot de passe ajouté avec succès !')
                print(f"Le mot de passe ajouté est : {new_password}")
                break

    elif option == '2':
        display_passwords()

    elif option == '3':
        print('Quitter le programme')
        break

    else:
        print('Option non valide. Veuillez sélectionner à nouveau.')