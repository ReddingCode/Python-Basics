# Les Colections
# Plusieurs elements
# Les tuples () : immutables --> Non modifiables
# Les Listes [] : mutable --> Modifiable

a = 5
b = 'Malick'

personnes = ('Malick', 'Maodo', 'Asse', 'Anta', 'Fatou')
print(len(personnes))
print(personnes[-1])  # on recupere le dernier element

# Les deux boucle for font la meme chose
for i in range(0, len(personnes)):
    print(personnes[i])

for i in personnes:
    print(i)
    print(len(i))
    print(i[-1])

valeurs = range(0, 5)
print(valeurs[-1])  # ca va afficher 4
