

# noms = []

# while True:
#     nom = input("Rentrer un nom...? ")
#     noms.append(nom)
#     if nom == "":
#         break
# del noms[-1]
# print(f"Les noms sont: {noms}")

noms = []

while True:
    nom = input("Rentrer un nom...? ")
    if nom == "":
        break
    noms.append(nom)


print(f"Les noms sont: {noms}")
noms.sort()  # trier les noms dans l'ordre alphabetique
