pares = 0
impares = 0
numeros_pares = []
numeros_impares = []

for i in range(10):
    try:
        numero = int(input("Digite um número: "))
        
        if numero < 0:
            print("Digite números positivos e inteiros")
            
            
        if numero % 2 == 0:
            pares += 1
            numeros_pares.append(numero)
        else:
            impares += 1
            numeros_impares.append(numero)
            
    except ValueError:
        print("Por favor, digite apenas números inteiros.")


print("Números pares:", numeros_pares)
print("Quantidade de números pares:", pares)
print("Números ímpares:", numeros_impares)
print("Quantidade de números ímpares:", impares)

