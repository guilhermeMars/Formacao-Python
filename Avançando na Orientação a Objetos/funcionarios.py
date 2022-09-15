class Funcionario:
    def __init__(self, nome):
        self.nome = nome

    def registra_horas(self, horas):
        print('Horas registradas...')

    def mostrar_tarefas(self):
        print('Fez muita coisa...')

class Caelum(Funcionario):
    def mostrar_tarefas(self):
        print('Fez muita coisa, Caelumer')

    def busca_cursos_do_mes(self, mes=None):
        print(f'Mostrando cursos - {mes}' if mes else 'Mostrando cursos desse mês')

class Alura(Funcionario):
    def mostrar_tarefas(self):
        print('Fez muita coisa, Alurete!')

    def busca_perguntas_sem_resposta(self):
        print('Mostrando perguntas não respondidas do fórum')

# Mixin
# Compartilha alguns comportamentos, sem ser os principais, e pode compartilhar com qualquer classe
# São classes que não foram feitas para serem instanciadas
class Hipster:
    def __str__(self):
        return f'Hipster, {self.nome}'

class Junior(Alura):
    pass

class Pleno(Alura, Caelum):
    pass

class Senior(Alura, Caelum, Hipster):
    pass


jose = Junior("Jose")
jose.busca_perguntas_sem_resposta()

marco = Pleno("Marco")
marco.mostrar_tarefas()

clara = Senior("Clara")
print(clara)


# MRO
# Ordem de prioridade das funções (do pleno)
# Pleno > Alura (primeiro herdado) > Funcionario (mãe da Alura) > Caelum > Funcionario (mãe do Caelum)
# Quando eles herdam da mesma mãe, o Funcionario é colocado no final, ficando
# Pleno > Alura > Caelum > Funcionario (mãe de Alura e Caelum)
