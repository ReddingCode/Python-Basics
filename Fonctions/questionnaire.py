print("************ QUESTIONS *************")
# print("Question: Quelle est l acapital de la France... ? ")
# print('a Marseille')
# print('b Nice')
# print('c Paris')
# print('d Nantes')
# reponse = input("Votre Reponse : ")
# if reponse == 'c':
#     print("Bonne reponse")
# else:
#     print("Mauvaise reponse")

# print("Question: Quelle est l acapital de l'Italie... ? ")
# print('a Rome')
# print('b Milan')
# print('c Naples')
# print('d Nantes')
# reponse = input("Votre Reponse : ")
# if reponse == 'a':
#     print("Bonne reponse")
# else:
#     print("Mauvaise reponse")

# print("Question: Quelle est l acapital du Sénégal... ? ")
# print('a Marseille')
# print('b Thies')
# print('c Louga')
# print('d dakar')
# reponse = input("Votre Reponse : ")
# if reponse == 'd':
#     print("Bonne reponse")
# else:
#     print("Mauvaise reponse")

# print("Question: Quelle est l acapital de la Mali... ? ")
# print('a Gambie')
# print('b Nice')
# print('c Bamako')
# print('d Pikine')
# reponse = input("Votre Reponse : ")
# if reponse == 'c':
#     print("Bonne reponse")
# else:
#     print("Mauvaise reponse")

QUESTIONS = (
    (("Question: Quelle est l acapital de la Mali... ? "),
     ('Gambie', 'Nice', 'Bamako', 'Pikine'), 'Bamako'),
    (("Question: Quelle est l acapital de l'Itali... ? "),
     ('Rome', 'Nice', 'Bamako', 'Pikine'), 'Rome'),
    (("Question: Quelle est l acapital du Sénégal... ? "),
     ('Rome', 'Dakar', 'Bamako', 'Pikine'), 'Dakar'),
    (("Question: Quelle est l acapital de la France... ? "),
     ('Marseille', 'Dakar', 'Paris', 'Pikine'), 'Dakar'),
)

score = 0


def questionnaire(question, choix, reponse):
    global score
    print(question)
    print(f' a - {choix[0]}')
    print(f' b - {choix[1]}')
    print(f' c - {choix[2]}')
    print(f' d - {choix[3]}')
    reponse_str = input("Votre Reponse : ")
    if reponse_str.lower() == reponse.lower():
        print("Bonne reponse")
        score += 1
    else:
        print("Mauvaise reponse")


for question in QUESTIONS:
    questionnaire(question[0], question[1], question[2])

print(f"Le score final est {score}/{len(QUESTIONS)} points")
