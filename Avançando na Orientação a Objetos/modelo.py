class Programa:
    def __init__(self, nome, ano):
        # Utilizar apenas 1 "_" faz com que mostre para o programador que este atributo é privado, mas não faz o name mangeling (alteração do nome pelo python)
        # Ajuda na hora de fazer a herança de classes, pois assim as classes filhas conseguem acessar o atributo
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0
    
    @property
    def likes(self):
        return self._likes

    def dar_like(self):
        self._likes += 1

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, novo_nome):
        self.nome = novo_nome.title()

    # def imprime(self):
    #     print(f"Nome: {self._nome} - Ano: {self.ano} - Likes: {self._likes}")

    # __str__ - Dumber para strings 
    def __str__(self):
        return f"Nome: {self._nome} - Ano: {self.ano} - Likes: {self._likes}"

class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        # super é o que chama a classe mãe
        # Dessa forma é chamado o inicializador da classe mãe, passando os atributos nome e ano
        super().__init__(nome, ano) 
        self.duracao = duracao

    def __str__(self):
        return f"Nome: {self._nome} - Ano: {self.ano} - Duração: {self.duracao} min - Likes: {self._likes}"

class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano) 
        self.temporadas = temporadas

    def __str__(self):
        return f"Nome: {self._nome} - Ano: {self.ano}- Temporadas: {self.temporadas} - Likes: {self._likes}"

class Playlist:
    def __init__(self, nome, programas):
        self.nome = nome
        self._programas = programas
    
    # Duck Typing - implementa um tipo de comportamento
    # Tem MUITOS desses, vale a pena pesquisar (Python Data Model)
    def __getitem__(self, item): # Representa uma sequência iterável
        return self._programas[item]

    def __len__(self): # Representa o sizable do objeto
        return len(self._programas)

    @property
    def listagem(self):
        return self._programas


# Funcionalidades de usar a biblioteca list (Além do for)

# Herança evita de escrever muito código
# class Playlist(list):
# print(f'Tamanho da playlist: {len(fim_de_semana)}')
# print(f"Vingadores? {vingadores in fim_de_semana}")


vingadores = Filme("vingadores guerra infinita", 2018, 160)
vingadores.dar_like()
vingadores.dar_like()
vingadores.dar_like()
tmep = Filme("todo mundo em pânico", 1999, 100)
tmep.dar_like()
tmep.dar_like()

atlanta = Serie("Atlanta", 2017, 2)
atlanta.dar_like()
tdoc = Serie("Todo mundo odeia o Cris", 2014, 3)
tdoc.dar_like()
tdoc.dar_like()
tdoc.dar_like()
tdoc.dar_like()
# print(f"Nome: {atlanta.nome} - Ano: {atlanta.ano} - Temp: {atlanta.temporadas} - Likes: {atlanta.likes}")

filmes_series = [vingadores, atlanta, tdoc, tmep]
fim_de_semana = Playlist('Fim de Semana', filmes_series)

# Polimorfismo
# Vantagem de percorrer uma lista utilizando da estrutura parecida dos filhos
for programa in fim_de_semana:
    # detalhes = programa.duracao if hasattr(programa, 'duracao') else programa.temporadas # hasattr - has atributte

    # Não importa qual o tipo, ele vai imprimir certo, pois os dois possuem seu método específico
    #programa.imprime()

    # Funciona por conta do __str__
    print(programa)

print(f'Tamanho da playlist: {len(fim_de_semana)}')
print(f"Vingadores? {vingadores in fim_de_semana}")
