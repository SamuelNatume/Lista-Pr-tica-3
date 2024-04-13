
while True:
    try:
        print("Digite 0 para sair: ")
        num = int(input("Digite um valor inteiro de 1 a 10: "))
        if num == 0:
            print("Você saiu!")
            break

        if 1 <= num <= 10:
            print(f"Tabuada do {num}")
            for numtab in range(0,11):
                mul= num*numtab
                print(f"{num} X {numtab} = {mul}")
        else:
            print("O número tem que ser inteiro entre 1 a 10. Tente novamente!")
    except ValueError:
        print("Por favor, digite apenas números inteiros.")