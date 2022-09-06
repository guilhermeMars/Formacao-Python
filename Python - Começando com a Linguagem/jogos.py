from forca import jogar_forca
from adivinhacao import jogar_adivinhacao

def jogos():
    print("Escolha o seu jogo!")
    print("----------------------------------")

    print("(1) Forca", "(2) Adivinhação", sep="\n")

    jogo = int(input("Qual jogo?"))

    if(jogo == 1):
        jogar_forca()
    elif(jogo == 2):
        jogar_adivinhacao()
    else:
        print("Erro")

if(__name__ == "__main__"):
    jogos()