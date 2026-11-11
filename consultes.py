from ciutats import ciutats

codi = input("Introdueix un codi postal: ")

trobat = False

for ciutat, dades in ciutats.items():
    if dades["codi_postal"] == codi:
            print("La ciutat és:", ciutat)
            trobat = True
if trobat == False:
    print("No s'ha trobat cap ciutat")
