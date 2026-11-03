"""Exercici 1.1. Hola Món! (personalitzat)
Crea el teu primer programa que mostri "Hola Món!" per pantalla
Modifica'l perquè mostri el teu nom i el poble o ciutat on vius, en línies separades
Afegeix una tercera línia que mostri una frase utilitzant el caràcter \t (tabulador) enmig del text
Comenta cada línia explicant què fa (amb les teves paraules, no repetint l'enunciat)"""

# Aqui utilitzo el print amb una cadena de text de hello world i "\n" 
# perque quedi millor estructurat

print("\nHello world\n")

# Aqui faig un print amb una cadena de text amb el meu nom i ciutat on visc 
# també utilitzo "\n" per separar lìnies

print("Yoel Ismael Polanco Ovando\nEspanya Barcelona Manresa\n")

# Aqui fem un print amb una cadena de text on dins 
# utilitzem el "\t" per fer un espai de tab i "\n"

print("això es un \ttab\n")

"""Crea una variable amb el teu nom, una amb la teva edat i una amb l'any en què vas començar aquest cicle
Mostra un missatge que utilitzi les tres variables en una sola frase amb print(), i print(f)
Afegeix una quarta variable calculada: quants anys faràs quan acabis el cicle (has de calcular-ho amb una operació, no escriure el número directament)
Comenta quin tipus de dada (int, str...) té cada variable"""

# str
nom = "Yoel Ismael "
# int
edat = 19
# int
ini_cicle = 2026
# str
espai = " "
# int
anys_per_cursar = 2

# fem u print on dins sumem les variables per mostrarles totes juntes i transformem els int a str

print((nom) + str(edat) + (espai) + str(ini_cicle))

# aqui utilitzó el (f"") per convinar text

print(f"\nEl meu nom és {nom} i la meva edat és {edat} i vaig començar el cicle el {ini_cicle}\n")

# aqui utilitzó (f"") i dins faig la suma de edat més anys de curs

print(f"quan acabi el cicle tindré {edat + anys_per_cursar}")