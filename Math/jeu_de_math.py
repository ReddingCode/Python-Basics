import random

NOMBRE_MIN = 1
NOMBRE_MAX = 10
NB_QUESTION = 4


def poser_question():
    a = random.randint(NOMBRE_MIN, NOMBRE_MAX)
    b = random.randint(NOMBRE_MIN, NOMBRE_MAX)
    o = random.randint(0, 3)

    operateur = "+"
    if o == 0:
        operateur = "+"
    # Si o == 1 , on change l'operateur avec '*'
    elif o == 1:
        operateur = "*"
    elif o == 2:
        operateur = "-"
    else:
        operateur = "/"
    # Ici on calcule 'a' (operateur) 'b'
    print(f"Calculez: {a} {operateur} {b}")
    reponse_str = input("Quel est le resultat...? ")
    calcul = a + b
    # Si o == 1 , on change l'operation avec a*b
    if o == 1:
        calcul = a * b

    # Ici on verifie est ce que le resultat est bonne
    if int(reponse_str) == calcul:
        return True

    return False


nb_points = 0
for i in range(0, NB_QUESTION):
    print(f"Vous avez {i+1}/{NB_QUESTION}")
    if poser_question():
        print("Bravooo!, Vous avez Trouvé")
        nb_points += 1
    # print("Oops!, Vous avez perdu...!")
    print()

moyenne = int(nb_points/2)
print(f"Vous avez {nb_points} points / {NB_QUESTION} ")
if nb_points == NB_QUESTION:
    print("Excellent!")
elif nb_points == 0:
    print("Revisez vos math")
elif nb_points > moyenne:
    print("Pas mal")
else:
    print("Peut mieux faire")
