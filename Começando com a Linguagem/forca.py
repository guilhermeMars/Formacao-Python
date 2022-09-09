from random import randrange


def jogar_forca():
    
    mensagem_inicial()

    palavra_secreta = gera_palavra_secreta()

    letras_acertadas = gera_letras_acertadas(palavra_secreta)
    print(letras_acertadas)
    
    enforcou = False
    acertou = False
    erros = 0

    while(not enforcou and not acertou):

        # Existem diversas funções boas de formatação na documentação, sempre vale a pena dar uma olhada

        chute = pede_chute()
        
        if(chute in palavra_secreta):
            chute_correto(palavra_secreta, chute, letras_acertadas)
        else:
            erros += 1
            desenha_forca(erros)
            print("Você errou! Ainda possui {} tentativas".format(7 - erros))
        
        enforcou = erros == 7 # Caso tenha passado 6 tentativas, retorna true e o jogo acaba
        acertou = "_" not in letras_acertadas

    if(acertou):
        print("Você ganhou!")
    else:
        print("Você perdeu!\nA palavra era {}".format(palavra_secreta))


# Funções

def mensagem_inicial():
    print("Bem vindo ao jogo de forca!!")
    print("----------------------------------")

def gera_palavra_secreta():
    arquivo = open("palavras.txt", "r") # r - Read, w - Whrite (cria um arquivo), a - Append (adiciona novos dados a um arquivo existente)
    palavras = []

    for linha in arquivo:
        palavras.append(linha.strip()) # Strip retira o \n
    
    arquivo.close()

    #palavra_secreta = palavras[randrange(0,len(palavras))]
    numero = randrange(0,len(palavras))
    palavra_secreta = palavras[numero].lower()
    return palavra_secreta

def gera_letras_acertadas(palavra):
    return ["_" for letra in palavra] # List Comprehensions (https://cursos.alura.com.br/course/python-3-avancando-na-linguagem/task/25539)
    # for letras in palavra_secreta:
    # letras_acertadas.append("_")

def pede_chute():
    chute = input("Qual a letra? ")
    chute = chute.strip().lower() # Tira espaços adicionais e deixa em minúsculo
    return chute

def chute_correto(palavra, chute, acertos):
    posicao = 0
    for letra in palavra:
        if(chute.lower() == letra.lower()): # Coloca os dois como minúsculo
            acertos[posicao] = chute
        posicao += 1
    quantidade_acertada = acertos.count(chute)
    print("{}\nVocê acertou {} letras".format(acertos, quantidade_acertada))

def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()

# Inicializa caso seja executado

if(__name__ == "__main__"):
    jogar_forca()