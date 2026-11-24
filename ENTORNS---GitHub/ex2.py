"""
2. Tots els elements sense duplicats   (1 punt)
Amb els mateixos conjunts de l'exercici 1, mostreu un conjunt nou amb tots els elements dels dos conjunts, sense repetir-ne cap.
Sortida esperada
{70, 40, 10, 50, 20, 60, 30}

"""
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}

print(set1 | set2)