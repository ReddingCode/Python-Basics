

CONVERSIONS = (
    ('pouces', 'cm', 2.54),
    ('m', 'cm', 100),
    ('km', 'miles', 0.621371),
    ('yard', 'm', 0.9144),
    ('kg', 'livres', 2.20462),
)


def demande_et_afficher_conversion(unit1, unit2, facteur, reverse: bool = False):
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


def demande_valeur_numerique_utilisateur(valeur_min, valeur_max):
    v = input(f"Donnez un valeur entre {valeur_min} et {valeur_max}... ")
    try:
        v_int = int(v)
    except:
        print("Erreur: Vous devez rentrer un valeur numerique")
        return demande_valeur_numerique_utilisateur(valeur_min, valeur_max)
    if not (valeur_min <= v_int <= valeur_max):
        print(
            f"Erreur: Vous devez rentrer un valeur (entre 1 et {valeur_max})")
        return demande_valeur_numerique_utilisateur(valeur_min, valeur_max)
    return v_int


print("********** Bienvenue dans le programme convertisseur ***********")
i = 1
for c in CONVERSIONS:
    unit1 = c[0]
    unit2 = c[1]
    print(f"{i} - {unit1} vers {unit2}")
    i += 1
    print(f"{i} - {unit2} vers {unit1}")
    i += 1
valeur_choix_max = i-1

choix_int = demande_valeur_numerique_utilisateur(1, valeur_choix_max)


while True:
    # Demander les valeur a convertir à l'demande_valeur_numerique_utilisateur

    # Si le choix d'utilisateur est 1 alors l'index est 0 le premier item de CONVERSIONS
    # Divise par 2 , car on génère des options intermédiaire de conversion inverse
    # choix = 2 --> index = 0, mais reverse = True (conversion inverse)
    index = (choix_int) // 2
    # 1 % 2 = 0 x 2 + 1 Si on divise 1 par 2, on obtient 0.5 (donc on prend 0), il nous reste 1
    # 2 % 2 = 1 x 2 + 0 Si on divise 2 par 2, on obtient 1 (donc on prend 0), il nous reste 0
    # 3 % 2 = 1 x 2 + 1 Si on divise 3 par 2, on obtient 1.5 (donc on prend 1), il nous reste 1
    # 4 % 2 = 2 x 2 + 0
    # True si la valeur est pair
    # On fait choix_int / 2 , on verifie s'il reste 0 , si oui c'est pair donc le reverse se sera true
    reverse = choix_int % 2 == 0
    unit1, unit2, facteur = CONVERSIONS[index]
    if demande_et_afficher_conversion(unit1, unit2, facteur, reverse):
        break
