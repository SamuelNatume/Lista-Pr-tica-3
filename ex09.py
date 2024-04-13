lista = []
for i in range(1,11):
    numero = float(input(f"Digite número {i}: "))
    if numero == int(numero):
        lista.append(numero)
    else:
        print("Digite apenas números inteiros!")    
        continue
lista.sort()
print(lista)    