from functools import total_ordering

## Total ordering
# Faz com que, ao implementar uma funcao de igualdade (__eq__) 
# E apenas uma funcão comparativa (__lt__, __gt__, __le__ etc)
# O total_ordering lida para criar todas as outras funções

@total_ordering
class ContaSalario():
    def __init__(self, cod):
        self.cod = cod
        self._saldo = 0
    
    def deposita(self, valor):
        self._saldo += valor
    
    def __eq__(self, eq):
        return self.cod == eq.cod 

    def __str__(self):
        return f"Código {self.cod}\nSaldo: {self._saldo}"
    
    # Lower Than = lt
    def __lt__(self, outro):
        # O if existe para caso eles sejam iguais
        if self._saldo != outro._saldo:
            return self._saldo < outro._saldo
        else:
            return self.cod < outro.cod

conta_guilherme = ContaSalario(15)
conta_guilherme.deposita(500)

conta_dani = ContaSalario(3)
conta_dani.deposita(1000)

conta_marco = ContaSalario(133)
conta_marco.deposita(510)

contas = [conta_guilherme, conta_dani, conta_marco]

# Saiba mais sobre sorted no outros_builtins.py
for conta in sorted(contas):
    # Dentro do for ele mostra o __str__ dos objetos
    print(conta)

# Funções implementadas pelo total_ordering
# Note que não temos uma função __le__ ou __ge__
conta_guilherme <= conta_marco
conta_guilherme >= conta_guilherme



# ## attrgetter

# # pega um atributo em específico
# from operator import attrgetter

# # Saiba mais sobre sorted no outros_builtins.py
# for conta in sorted(contas, key=attrgetter("_saldo")):
#     print(conta)
