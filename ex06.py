no_intervalo = 0
fora_intervalo = 0

for i in range(10):
    try:
        numero = int(input("Digite um número: "))

        if 10 < numero < 20:
            no_intervalo += 1
        
        else:
            fora_intervalo += 1
    except ValueError:
        print("Por favor, digite apenas números inteiros.")
    
    print("Números dentro do intervalo de 10 a 20:", no_intervalo)
    print("Números fora do intervalo:" , fora_intervalo)
