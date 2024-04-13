numero = int(input("Digite um número positivo: "))
if numero <= 0:
    print("O número digitado não é positivo.")
    
else:
    print(f"Os divisores de {numero} são: ")
    for divisor in range(1, numero + 1):
        if numero % divisor == 0:
            print(divisor)