# Tester si une chaine contient des chiffres
# any / isdigit

# On verifie , y'a pas de nombre dans le text saisi
def chaine_contient_chiffre(chaine):
    """for c in chaine:
        if c.isdigit():
            return True
    return False"""
    # Fonction 'any()', nous permet de simplifie le code en un seule ligne
    return any([c.isdigit() for c in chaine])


nom = input("Quel est ton nom ? ")
if nom == "":
    print("Le nom est vide")
elif chaine_contient_chiffre(nom):
    print("Ce nom est invalide, il ne doit pas contenir de chiffres")
else:
    print("Bonjour " + nom)
