from bytebank import Funcionario

guilherme = Funcionario('Guilherme Martins', '07/07/2004', 2000)
print(guilherme)
print(guilherme.idade())

# Teste automatizado
def teste_idade():
    funcionario_teste = Funcionario('teste', '07/07/2004', 1111)
    print(f'Teste = {funcionario_teste.idade()}')

teste_idade()
