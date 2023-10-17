palavra = "plantas"
tentativas = 7
chute = []
ganhando = 0

print("Você consegue advinhar a palavra oculta? Cuidado para não ser enforcado!")
while True:
    for letra in palavra:
        if letra in chute:
            print(letra, end=" ")

        else:
            print("_", end="")
    print(end=" ")
    letra_dig = input(f"restam {tentativas} tentativas\n "
                       "Você chuta que letra?  ")
    chute.append(letra_dig)
    if letra_dig not in palavra:
        tentativas -= 1
    if tentativas == 6:
        print("---------\n"
              "|       |\n"
              "|       @\n"
              "|\n"
              "|\n"
              "|\n"
              "|\n")
    elif tentativas == 5:
        print("---------\n"
              "|       |\n"
              "|       @\n"
              "|      /\n"
              "|\n"
              "|\n"
              "|\n")
    elif tentativas == 4:
        print("---------\n"
              "|       |\n"
              "|       @\n"
              "|      /|\n"
              "|\n"
              "|\n"
              "|\n")
    elif tentativas == 3:
        print("---------\n"
              "|       |\n"
              "|       @\n"
              "|      /|\ \n"
              "|\n"
              "|\n"
              "|\n")
    elif tentativas == 2:
        print("---------\n"
              "|       |\n"
              "|       @\n"
              "|      /|\ \n"
              "|       |\n"
              "|\n"
              "|\n")
    elif tentativas == 1:
        print("---------\n"
              "|       |\n"
              "|       @\n"
              "|      /|\ \n"
              "|       |\n"
              "|      /\n"
              "|\n")
    elif tentativas == 0:
        print("---------\n"
              "|       |\n"
              "|       @\n"
              "|      /|\ \n"
              "|       |\n"
              "|      / \ \n"
              "| VOCÊ PERDEU!\n")
        break
    ganhou = True
    for letra in palavra:
        if letra not in chute:
            ganhou = False

    if ganhou:
        print(f"VOCÊ GANHOU! A palavra foi {palavra}")
        break
