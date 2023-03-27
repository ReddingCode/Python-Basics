
import random

NOMBRE_MAX = 10
NOMBRE_MIN = 1
NOMBRE_MAGIQUE = random.randint(NOMBRE_MIN, NOMBRE_MAX)
NB_VIES = 4
# vie = NB_VIES


def demander_nombre(nb_min, nb_max):
    nombre_int = 0
    while nombre_int == 0:
        nombre_str = input(
            f"Quel est le nombre magique entre {nb_min} et {nb_max}...?  ")
        try:
            nombre_int = int(nombre_str)
        except ValueError:
            print("Erreur: Vous devez rentrer un nombre valide, Ressayez")
        else:
            if nombre_int < nb_min or nombre_int > nb_max:
                print(f"Erreur: Le nombre doit etre entre {min} et {max}")
                nombre_int = 0

    return nombre_int


# nombre = 0
# while not nombre == NOMBRE_MAGIQUE and vie > 0:
#     print(f"Il vous reste {vie} de vies")
#     nombre = demander_nombre(NOMBRE_MIN, NOMBRE_MAX)
#     #     print("Erreur: Vous devz rentrer un nombre valide")
#     if nombre > NOMBRE_MAGIQUE:
#         print("Le nombre magique est plus petit")
#         vie -= 1
#     elif nombre < NOMBRE_MAGIQUE:
#         print("Le nombre magique est plus grand")
#         vie -= 1
#     else:
#         print("Vous avez gagné")

# if vie == 0:
#     print(f"Vous avez perdu !, Le nombre magique etait {NOMBRE_MAGIQUE}")
gagne = False

for i in range(0, NB_VIES):
    vies = NB_VIES - i
    print(f"Il vous reste {vies} de vies")
    nombre = demander_nombre(NOMBRE_MIN, NOMBRE_MAX)
    #     print("Erreur: Vous devz rentrer un nombre valide")
    if nombre == NOMBRE_MAGIQUE:
        print("Bravo ! ,Vous avez gagné")
        gagne = True
        break
    elif nombre < NOMBRE_MAGIQUE:
        print("Le nombre magique est plus grand")

    else:
        print("Le nombre magique est plus petit")


if not gagne:
    print(f"Vous avez perdu !, Le nombre magique etait {NOMBRE_MAGIQUE}")
