# Les Colections
# Plusieurs elements
# Les tuples () : immutables --> Non modifiables
# Les Listes [] : mutable --> Modifiable

# a = 5
# b = 'Malick'

# personnes = ['Malick', 'Maodo', 'Asse', 'Anta', 'Fatou']
# print(len(personnes))


# def afficher_personnes(c):
#     for i in c:
#         print(i)


# def modifier_a(a):
#     a = 10


# test = 5
# print(test)
# test = modifier_a(test)
# print(test)  # La valeur 5 ne changera pas


# def modifier_a_avec_liste(a):
#     a[0] = 10
#     print(a)


# test = [5, 3, 7, 9]
# print(test)
# test = modifier_a_avec_liste(test)
# print(test)  # La valeur 5 va changera


################### TUPLES AVEC FONCTION ###################

def obtenir_infopersonnes():
    return 'Mami', 19, 1.70


def afficher_info_personnes(nom, age, taille):
    print(f"Informations: Nom: {nom}, Age: {age}, Taille: {taille}")


infos = obtenir_infopersonnes()
afficher_info_personnes(*infos)
print(f"Nom: {infos[0]}")
print(f"Age: {infos[1]}")
print(f"Taille: {infos[2]}")

nom, age, taille = obtenir_infopersonnes()
print(print(f"Informations: Nom: {nom}, Age: {age}, Taille: {taille}"))
