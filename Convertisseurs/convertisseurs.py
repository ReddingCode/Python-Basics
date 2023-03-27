"""
1 pouce = 2.54 cm
2 cm = 0.394 pouces

Exemple :
Un ecran de 17 pouces de diagonale, correspond à 43,18 cm (=17*2,54)

Voici comment votre programme doit se comporter :
1 - Demander à l'utilisateur si il souhaite convertir de "pouces vers cm" ou "cm vers pouces"
2 - Demander à l'utilisateur de rentrer la valeur à convertir (en precisant l'unité)
3 - Afficher la valeur convertie (et l'unité : cm ou pouces )
- Fin du programmme
"""

# print("********** Bienvenue dans le programme convertisseur ***********")
# print("1 - pouces vers cm")
# print("2 - cm pouces vers ")
# choice = input("Quel est votre choix...? ")
# pouce = 2.54
# cm = 0.394
# if int(choice) == 1:
#     print("pouces vers cm")
#     reponse = input("Quel est le valeur de pouces à convertir en cm...? ")
#     try:
#         reponse_int = int(reponse)
#         result = reponse_int * cm
#         print(f"La valeur de {reponse_int} en pouce egale à {result} cm")
#     except ValueError:
#         print("Erreur: La valeur n'est pas valable")

# else:
#     print("cm vers pouces  ")
#     reponse = input("Quel est le valeur de cm à convertir en pouces...? ")
#     try:
#         reponse_int = int(reponse)
#         result = reponse_int * pouce
#         print(f"La valeur de {reponse_int} en cm egale à {result} pouces")
#     except ValueError:
#         print("Erreur: La valeur n'est pas valable")

"""
A -> B
    x2
5a -> 10b

B -> A
    0.5(1/2)
10b -> 5a

"""


def convertisseur(unit1, unit2, facteur, reverse: bool = False):
    if reverse:
        unit1, unit2 = unit2, unit1
        facteur = 1/facteur
    valeur_str = input(
        f"Conversions {unit1} vers --> {unit2} Donnez la valeur en {unit1} ou ('q' pour quitter)...: ")
    if valeur_str == "q":
        return True
    try:
        valeur_float = float(valeur_str)
    except ValueError:
        print("Erreur: vous devez rentrer un nombre numérique")
        print("Utilisez un point et non une virgule pour les décimale")
        return convertisseur(unit1, unit2, facteur)

    valeur_convertis = round(valeur_float * facteur, 2)
    print(
        f"Résultat de conversion : {valeur_float}  {unit1} = {valeur_convertis} {unit2} ")
    return False


while True:
    print("********** Bienvenue dans le programme convertisseur ***********")
    print("1 - pouces vers cm")
    print("2 - cm pouces vers ")
    choice = input("Quel est votre choix...? ")
    if choice == '1' or choice == '2':
        break
    print("Vous devez rentrer (1 ou 2)")

while True:
    if convertisseur('pouces', 'cm', 2.54, reverse=False if choice == '1' else True):
        break

# def convertisseur(pouces, cm):
#     if demander_choix():

#         print("pouces vers cm")
#         reponse = input("Quel est le valeur de pouces à convertir en cm...? ")
#         try:
#             reponse_int = int(reponse)
#             result = reponse_int * cm
#             print(f"La valeur de {reponse_int} en pouce egale à {result} cm")
#         except ValueError:
#             print("Erreur: La valeur n'est pas valable")

#     else:
#         print("cm vers pouces  ")
#         reponse = input("Quel est le valeur de cm à convertir en pouces...? ")
#         try:
#             reponse_int = int(reponse)
#             result = reponse_int * pouces
#             print(f"La valeur de {reponse_int} en cm egale à {result} pouces")
#         except ValueError:
#             print("Erreur: La valeur n'est pas valable")
