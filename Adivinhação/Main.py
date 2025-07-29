import random
def main():
    numeroAleatorio = random.randint(0, 10)

    numero = -1

    i = 0

    while numeroAleatorio != numero:

        numero = int (input ("Digite um número: "))

        if numero > numeroAleatorio:
            print("O seu número é maior")
        elif numero < numeroAleatorio:
            print("O seu número é menor")
        
        i += 1
    
    print("Você acertou com ", i, " tentativas")



    return 0
main()