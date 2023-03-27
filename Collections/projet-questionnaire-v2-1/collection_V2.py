# LES FONCTIONS : PROJET QUESTIONNAIRE
#
# Question : Quelle est la capitale de la France ?
# (a) Marseille
# (b) Nice
# (c) Paris
# (d) Nantes
#
# Votre réponse :
# Bonne réponse / Mauvaise réponse

# ...
# Question : Quelle est la capitale de l'Italie ?
# ...
#
# 4 questions

def demande_reponse_numerique_utilisateur(min, max):
    reponse_str = input(f"Votre réponse (entre 1 et {max}): ")
    try:
        reponse_int = int(reponse_str)
        if min <= reponse_int <= max:
            return reponse_int
        print(
            f"Erreur: Vous devez rentrer un nombre entre ({min} et {max})")
    except:
        print("Erreur: Vous devez rentrer un nombre...")
    return demande_reponse_numerique_utilisateur(min, max)


def poser_question(questions):
    global score
    print("QUESTION")
    print(f"  {questions[0]}")
    choix = questions[1]
    for i in range(len(choix)):
        print(f" {i+1}-  {choix[i]}")

    # print("  ", choix[1])
    # print("  ", choix[2])
    # print("  ", choix[3])
    print()
    bonne_reponse = questions[2]
    reponse_correct = False

    reponse_int = demande_reponse_numerique_utilisateur(1, len(choix))
    if choix[reponse_int-1].lower() == bonne_reponse.lower():
        print("Bonne réponse")
        reponse_correct = True
    else:
        print("Mauvaise réponse")

    print()
    return reponse_correct


def lancer_questionnnaire(questions):
    score = 0
    for question in questions:
        if poser_question(question):
            score += 1
    print(f"Score final : {score} sur {len(questions)}")


'''
    questionnaire[]
        question
            titre = "Quelle est la capitale de la France ?"
            reponses = ("Marseille", "Nice", "Paris", "Nantes")
            bonne_reponse = "Paris"

'''

QUESTIONNAIRE = (
    ("Question: Quelle est l acapital de la Mali... ? ",
     ('Gambie', 'Nice', 'Bamako', 'Pikine'), 'Bamako'),
    ("Question: Quelle est l acapital de l'Itali... ? ",
     ('Rome', 'Nice', 'Bamako', 'Pikine'), 'Rome'),
    ("Question: Quelle est l acapital du Sénégal... ? ",
     ('Rome', 'Dakar', 'Bamako', 'Pikine'), 'Dakar'),
    ("Question: Quelle est l acapital de la France... ? ",
     ('Marseille', 'Dakar', 'Paris', 'Pikine'), 'Paris'),
)

lancer_questionnnaire(QUESTIONNAIRE)
