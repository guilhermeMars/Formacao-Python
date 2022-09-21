## Tupla #
# listas imutáveis, não podem ser alteradas
# Utilizadas quando cada posição possui um significado diferente

guilherme = ('Guilherme Martins', 18, 2004)
daniela = ('Daniela', 24, 1998)

# Funciona para mudar os dados, pois cria uma nova tupla
def deposita(conta):
    nova_idade = conta[1] + 1
    return (conta[0], nova_idade, conta[2])

# Na prática utilizamos tuplas e listas conforme o contexte, e em muitas aplicações usamos as duas
# Exemplos: https://cursos.alura.com.br/course/python-collections-listas-e-tuplas/task/52941