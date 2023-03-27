# LES COLLECTIONS : LISTES / TUPLES
# Operations sur les éléments : min, max, in, sum

#          0        1        2           3           4
noms = ["Jean", "Sophie", "Martin", "Christophe", "Zoe"]

ages = [21, 20, 30, 25, 22]

# On utilise 'in' pour verifier est ce que "31" est dans le liste "noms"
'''if 31 in ages:
    print("Présent")
else:
    print("Abscent") '''
# On verifier est ce que "Martin" est dans le liste "noms"
'''found = False
for nom in noms:
    if nom == "Martin":
        found = True
        break
if found:
    print("Présent")
else:
    print("Abscent")'''

print(sum(ages))  # La sommes de tout les ages

print(max(ages))  # Le plus grand
print(min(ages))  # Le plus petit
