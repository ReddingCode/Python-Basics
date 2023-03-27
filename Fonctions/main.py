

def est_majeur(age):
    if int(age) >= 18:
        return True
    return False


def afficher_infos_personnes(nom, age):
    if age == '':
        print(f"La personne {numero_personne} est {nom} ")
    print(f"La personne est {nom} son age est {age}")
    print(f"Son nom comporte {len(nom)} lettres")
    if est_majeur(age):
        print("Vous etes majeur")
    else:
        print("Vous etes mineur")


def recuperer_et_afficher_infos_personnes(numero_personne):
    nom = input(f'Le nom de la personne : {numero_personne}...?')
    age = input(f"Quel est votre age {nom}...? ")
    afficher_infos_personnes(nom, age)


nb_personnes = 3

for i in range(nb_personnes):
    recuperer_et_afficher_infos_personnes(i+1)


# recuperer_et_afficher_infos_personnes(1)
