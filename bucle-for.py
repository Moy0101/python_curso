cadena = input("de que palabra quieres contar la cantidad de vocales : ")
vocales = "aeiouAEIOU"
contador = 0

for char in cadena:
    if char in vocales:
        contador += 1

print("Número de vocales en la cadena:", contador)