# LES COLLECTIONS : LISTES / TUPLES
# Les compréhensions de listes

#          0        1        2           3           4      5
noms = ["Jean", "Sophie", "Martin", "Christophe", "Zoe", "Martin"]

'''longeur_noms = []
for nom in noms:
    longeur_noms.append(len(nom))

# On affiche le nombre de cractere d'un nom, si ils ont inferieur a 10
longeur_noms = [len(nom) if len(nom) < 10 else 0 for nom in noms]
# On recuper les mots qui contient au moin la lettre 'e'
noms_avec_e = [nom for nom in noms if "e" in nom]
print(longeur_noms)
print(noms_avec_e) '''

''' Ici on affiche les nombres impair, i diviser par 2 en entier(sans restant apres le virgule)
on le multiplie par 2 , on verifie est ce qu'il est different de lui meme '''
a = [i for i in range(11) if (i//2)*2 != i]
b = [(i, True if (i//2)*2 == i else False) for i in range(11)]

print(a)
print(b)
