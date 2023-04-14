import hashlib

def password_check(passwd):
    maj = ['A','B','C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    chiffres = ['0','1','2','3','4','5','6','7','8','9']
    caracterespecial = ['!','@','#','$','%','^','&','*']

    if len(passwd) >= 8 :
        if True in [car in maj for car in passwd]:
            if True in [car in chiffres for car in passwd]:
                if True in [car in caracterespecial for car in passwd]:
                    return True

    return False

id = input("Identifiant : ")
mdp = input("Mot de Passe : ")

if password_check(mdp) and mdp == "b":
    print("Bienvenue !!!")
else:
    print("Identifiant ou mot de passe incorrect.")
    confirm = input("Réentrez le mot de passe pour vérifier 😊 : ")
    if password_check(confirm) and confirm == "b":
        print("Bienvenue !!!")
    else:
        print("Mot de passe incorrect. Accès refusé.")

# Hashage d'une chaine de caractères avec l'algorithme SHA-256
string_to_hash = input("Entrez une chaine de caractères à hasher : ")
hash_object = hashlib.sha256(string_to_hash.encode())
hex_hash = hash_object.hexdigest()
print(f"Hash de la chaine '{string_to_hash}' : {hex_hash}")
