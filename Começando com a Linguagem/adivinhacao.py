# sep - adiciona algo entre os valores separador por vírgula
# end - adiciona algo no final do print
# print("Brasil", "ganhou", 5, "titulos mundiais", sep=" ", end="\n")
def jogar_adivinhacao():
    from random import randrange


    print("Bem vindo ao jogo de adivinhação!!")
    print("----------------------------------")

    numero_secreto = randrange(1, 101)
    total_tentativas = 0
    pontos = 1000

    print("Qual a dificuldade do jogo?")
    print("(1) Fácil", "(2) Médio", "(3) Difícil", sep="\n")

    nivel = int(input("Defina o nível: "))

    if(nivel == 1):
        total_tentativas = 15
    elif(nivel == 2):
        total_tentativas = 10
    elif(nivel == 3):
        total_tentativas = 5
    else:
        print("Digite um número")

    for rodada in range(1, total_tentativas+1) :
        # print("Tentativa", rodada, "de", total_tentativas, sep=" ")
        
        # String interpolation

        #print("Olá Sr.{1} {0}", Martins, Guilherme) - É possível alterar a ordem em que os valores são exibidos

        # {:7.2f} - 7 caracteres(no total), 2 depois do ponto, f número float (int - d)

        # Ex:
        # print("R$ {:7.2f}".format(4.5))
        # print("R$ {:7.2f}".format(2417.5))
        # print("Data: {2d}/{2d}".format(9,4))

        print("Tentativa {} de {}".format(rodada, total_tentativas))
        
        chute_str = input("Digite um número entre 1 e 100: ")
        chute = int(chute_str)

        if(chute < 1 or chute > 100):
            print("Você deve digitar um número entre 1 e 100")
            continue # Sai da iteração atual

        print("Você digitou: ", chute)

        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if(numero_secreto == chute):
            print("Você acertou! Você fez {} pontos".format(pontos))
            break # Quebra o laço
        elif(maior):
            print("Você errou! Seu número é maior")
            pontos_perdidos = abs(numero_secreto - chute) # abs - pega o número absoluto, não aceitando negativos
            pontos = pontos - pontos_perdidos
        elif(menor):
            print("Você errou! Seu número é menor")
            pontos_perdidos = numero_secreto - chute
            pontos = pontos - pontos_perdidos
        else:
            print("Erro!")
            break
    print("Game Over!")

if(__name__ == "__main__"): # Quando se roda diretamente o arquivo, internamente o python adiciona __main__ na variável __name__
    jogar_adivinhacao()