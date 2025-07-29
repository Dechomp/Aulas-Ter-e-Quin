def main():
    nome = input ("Digite o seu nome: ")
    quantIrmaos = int (input ("Digite quantos irmãos ou irmãs vc tem: "))
    altura = float (input("Digite a sua altura: "))
    isCabelo = input("Vc tem cabelo? ")

    print("O ", nome, "  tem ", quantIrmaos,  "e irmãos(ãs)", altura,  "de altura")

    if isCabelo  == "Sim" or isCabelo == "s":
        print("Ele possui cabelo")
    elif isCabelo == "Tenho"     :
        print("Ele tem cabelo")
    else:
        print("Ele não possui cabelo")



    return 0
main()