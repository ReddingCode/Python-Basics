def element_dans_liste(e, listes):
    # for el in listes:
    #     if e.lower() == el.lower():
    #         return True
    # return False
    l_Lower = [el.lower() for el in listes]
    return e.lower() in l_Lower


noms = ['jean', 'Sophie', 'Fatou', 'Malick', 'Cheikh', 'Fatyma']

# On cherche est ce que le nom 'Fatou' se trouve dans la liste
if element_dans_liste('Fatou', noms):
    print("L'element est la")
else:
    print("l'element n'est pas la")
