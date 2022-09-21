idades = [39, 30, 27, 18]
idades.append(15)
idades.remove(30)
# Sempre pocurar na documentação
idades.insert(0, 10) # Adiciona em uma posição específica
idades.extend([46, 78]) # Adiciona mais de um item na lista
# List comprehension
idades_prox_ano = [(idade + 1) for idade in idades] # Cria um novo array [] adicionando +1 nas idades
idades_maior_18 = [(idade) for idade in idades if idade > 18]

# Problemas das listas serem mutáveis: https://cursos.alura.com.br/course/python-collections-listas-e-tuplas/task/52938
# Em funções, caso a lista seja passada como parâmetro, o valor dela pode ser alterado
# Quando é utilizado um parâmetro default e são feitas alterações nesse parâmetro, toda vez que rodar a função, ele terá um valor diferente, pois está no cache da aplicação
def processamento_visualizacao(lista = None):
    if lista == None:
        lista = list()
    print(len(lista))
    print(lista)
    lista.append(13) 

print(idades)
print(f"Tem 15? {15 in idades}")
print(idades_prox_ano)
print(idades_maior_18)
# idades.clear()



class Conta():
    def __init__(self, cod):
        self.cod = cod
        self.saldo = 0
    
    def deposita(self, valor):
        self.saldo += valor

    def __str__(self):
        return f"Código {self.cod}\nSaldo: {self.saldo}"

conta_gui = Conta(15)
conta_gui.deposita(150)
print(conta_gui)

conta_dani = Conta(6385)
conta_dani.deposita(1000)
print(conta_dani)

contas = [conta_gui, conta_dani] # Quando adiciona um objeto em uma lista, não é criado uma outra instância do mesmo, e sim uma referência ao mesmo objeto
print(contas)
for conta in contas:
    print(conta)
