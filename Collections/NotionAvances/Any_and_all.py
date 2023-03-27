# LES COLLECTIONS : LISTES / TUPLES
# Any et All
# Any : Quelconque / n'importe quel
# All : Tous

#          0        1        2           3           4      5
noms = ["Jean", "Sophie", "Martin", "Christophe", "Zoe", "Martin"]

''' a = [True, True, False, True]
# Si tout le tableau y'a au moin un True, ca va returner True
print(any(a))
# Si tout le tableau est True, ca veut dire tout est True, il va retourner false
print(all(a)) '''


'''found = False
for nom in noms:
    if "z" in nom.lower():
        found = True
        break

if found:
    print("Trouvé")
else:
    print("Non trouvé")'''

# ça va affiche Non trouve, parceque y'a au moin un nom qui n'a pas de 'e'
# Si om met "any()", ca va retourner Trouve ,parceque y'a au moin un nom qui a 'e'
nom_avec_un_z_existe = all(
    [True if "e" in nom.lower() else False for nom in noms])
if nom_avec_un_z_existe:
    print("Trouvé")
else:
    print("Non trouvé")
