"""Part 2: Operadors bàsics (ex01-2.py)
Exercici 2.1: Python com a calculadora, provant (amb les teves dades)
En lloc dels números de l'enunciat clàssic, fes servir el dia i el mes del teu naixement (per exemple, si vas néixer el 14 de març: dia=14, mes=3):
dia = ...   # el teu dia de naixement
mes = ...   # el teu mes de naixement
print(dia + mes)
print(dia - mes)
print(dia * mes)

Abans d'executar, escriu en un comentari quin resultat esperes per a cada línia."""

dia = 27
mes = 1

# 28
print(dia + mes)
# 26
print(dia - mes)
# 27
print(dia * mes)

# 29, s'executa primer la multiplicació
print(dia + mes * 2)
# 56 es fa primer la suma perque esta entre parentesis
print((dia + mes) * 2)
# 81 es fa primer la divisió
print(dia / mes * 3)
# 27  es fa primer la divisió
print(dia + mes // 2)
#  es fa primer la potencia
print(dia ** 2 - mes)
