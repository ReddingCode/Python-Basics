# LISTES - ALGO : VALEUR PLUS PETITE

distance_chauffeur = ['Malick', 'Fatou',
                      'Cheikh', 'Maodo', 'Moussa', 'Ahmed', 'Mami']
distance_chauffeur_km = [1.5, 2.2, 0.4, 0.9, 7.1, 1.1, 0.6]

# distance_min = distance_chauffeur_km[0]

# for distance in distance_chauffeur_km:
#     if distance < distance_min:
#         distance_min = distance

# print(f"Distance minimale : {distance_min} km")

distance_min = distance_chauffeur_km[0]


for i in range(len(distance_chauffeur_km)):
    distance = distance_chauffeur_km[i]
    if distance < distance_min:
        distance_min = distance
        index_min = i

print(f"Distance minimale : {distance_min} km")

print(f"Index minimale : {index_min} ")
print(f"Le nom du chauffeur est: {distance_chauffeur[index_min]} ")

# distance_max = distance_chauffeur_km[0]

# for distance in distance_chauffeur_km:
#     if distance > distance_max:
#         distance_max = distance

# print(f"Distance maximale : {distance_max} km")
