frase = "Bem vindo meu nome é Guilherme eu gosto muito de nomes e tenho o meu cachorro e gosto muito de cachorro"
frase_minusculo = frase.lower()
frase_sem_espaco = frase_minusculo.split()

aparicoes = {}
for palavra in frase_sem_espaco:
    ate_agora = aparicoes.get(palavra, 0)
    aparicoes[palavra] = ate_agora + 1

print(aparicoes)

## Defaultdict
# Caso queira criar um dicionário com valor padrão
# Sem ter que usar o get("exemplo", 0)

from collections import defaultdict

# Precisa passar uma função, que será chamada toda vez que não tiver um valor
# Função int() devolve o valor 0 quando chamada sem parâmetro
aparicoes2 = defaultdict(int)

for palavra in frase_sem_espaco:
    # Não preccisa das outras linhas pois não tem o get
    aparicoes2[palavra] += 1

print(aparicoes2)

class Conta:
    def __init__(self):
        print("Criando conta")

# Caso não tenha uma conta, ele cria uma automaticamente
contas = defaultdict(Conta)
print(contas[15])
print(contas[18])
print(contas[3])

## Importância de olhar a documentação
# Já havia um Contador, não era nescessário implementar do zero

from collections import Counter

aparicoes3 = Counter(frase_sem_espaco)

print(aparicoes3)
    