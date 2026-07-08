numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numeros_impares = []

for numero in numeros:
    if numero % 2 != 0:
        numeros_impares.append(numero)

somatorio = sum(numeros_impares)
print (f'A soma dos números ímpares é: {somatorio}')