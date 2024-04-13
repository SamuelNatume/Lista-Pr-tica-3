


print("Quando quiser encerrar o programa e calcular a média digite '0'")
idades = [] 

while True:
    try:
        idade = int(input("Digite uma idade (ou '0' para encerrar e mostrar a média): "))

        if idade == 0:
            break

        elif idade < 0:
            print("Digite uma idade inteira positiva.")
            continue

        idades.append(idade) 

    except ValueError:
        print("Por favor, digite apenas números inteiros.")

if idades:  
    media = sum(idades) / len(idades)
    print("A média das idades é:", media)
else:
    print("Nenhuma idade foi inserida. Não é possível calcular a média.")
