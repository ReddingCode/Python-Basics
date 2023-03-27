
# def pizza_existe(e, pizzas):
#     for i in pizzas:
#         if i == e:
#             return True
#         return False

# existe = pizzas[:]
# for i in pizzas:
#     if i == existe:
#         print("Erreur ce pizza existe")
#     return True
# for i in pizzas:
#     if i == pizza:
#         print("Erreur ce pizza existe")
#         return


# Ajouter pizza pour utilisateur
def ajouter_pizza_utilisateur(pizzas):
    p = input("Ajouter un pizza...")
    if p.lower() in pizzas:
        print("Erreur ce pizza existe déja")
    else:
        if p != '':
            pizzas.append(p)

# Ca va trier en premier les mots les plus long


def personaliser(e):
    return len(e)


def afficher_pizzas(pizzas, affiche=0):
    ajouter_pizza_utilisateur(pizzas)
    print(f"######### VOICI LA LISTES DES PIZZAS {len(pizzas)} #########")
    if len(pizzas) == 0:
        print("AUCUN PIZZAS ...")
        # Je sort de la fonction
        return
    # Personnalise l'affichage avec la fonction sort()
    # pizzas.sort(reverse=True, key=personaliser)
    for i in pizzas:
        if affiche != 0:
            print(f"Pizza : {pizzas[:affiche]}")
            break
        print(f"Pizza : {i}")
    print()
    # On recupere le premiere et le derniere element
    print(f"Premiere pizza: {pizzas[0]}")
    print(f"Derniere pizza: {pizzas[-1]}")


PIZZAS = ['4 fromages', 'végétarinne', 'hawai', 'calzone']
# pizza_ajouter = PIZZAS.append(ajouter_pizza_utilisateur(PIZZAS))
# afficher_pizzas(pizza_ajouter)
# vide = ()
# afficher_pizzas(vide)
ajouter_pizza_utilisateur(PIZZAS)
afficher_pizzas(PIZZAS, 3)
