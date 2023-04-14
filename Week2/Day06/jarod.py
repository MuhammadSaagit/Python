def password_check(passwd):

    maj = ['A','B','C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    chiffres = ['0','1','2','3','4','5','6','7','8','9']
    caracterespecial = ['!','@','#','$','%','^','&','*']

id = input("Identifiant : ")
mdp = input("Mot de Passe : ")
mdp1 = "b"

if len(mdp) >= 8 :
    if True in(car in "maj" for car in mdp):
        if (car in "chiffres" for car in mdp):
            if (car in "caracterespcial" for car in mdp):
                if (mdp1 == ("b")):
                    print("Bienvenue !!!")

else:
    print("Invalid Password !!")

    if input("Réentrez le mot de passe pour vérifier 😊 == mdp:
        confirm = True


import hashlib

#La chaine de caractères à hasher
string_to_hash = "example_string"

#création d'un object hash SHA-256
hash_object = hashlib.sha256()

#Mise à jour de l'object hash avec la chaine de caractères à hasher
hash_object.update(string_to_hash.encode())

#Récupération du hash en hexadécimal
hex_hash = hash_object.hexdigest()

print(f"Hash de la chaine '{string_to_hash}' : {hex_hash}")

#Cela imprimera:
#Hash de la chaine 'example_string' : 6f1ed002ab5595859014ebygfdsf75f

if id == "a" and mdp == "b":
    print("Bienvenue")
elif id == "a" and mdp != "b":
    print("Mot de passe incorrect...")
elif id != "a" and mdp == "b":
    print("Identifiant incorrect...")