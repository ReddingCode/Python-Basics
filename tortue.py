import turtle

t = turtle.Turtle()

# t.forward(100)
# t.left(90)
# t.forward(50)
# t.backward(45)
# t.forward(200)

# t.right(90)
# t.forward(50)
# t.left(90)
# t.forward(50)


def escalier(taille, nb):
    for i in range(0, nb):
        t.forward(taille)
        t.left(90)
        t.forward(taille)
        t.right(90)
    t.forward(taille)


# escalier(40, 5)
def carre(taille, nb):
    for i in range(0, nb):
        # t.forward(taille)
        t.left(90)
        t.forward(taille)


def carres(taille_depart, nb):
    for i in range(0, nb):
        # carre(taille_depart, nb)
        # taille_depart += 20
        taille = (i+1) * taille_depart
        carre(taille, nb)


carre(50, 4)
# carres(20, 5)
turtle.done()
