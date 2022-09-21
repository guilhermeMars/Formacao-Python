## Herança e Polimorfismo

from abc import ABCMeta, abstractmethod # veja mais no @abstractmethod

class Conta(metaclass=ABCMeta):
    def __init__(self, cod):
        self.cod = cod
        self.saldo = 0
    
    def deposita(self, valor):
        self.saldo += valor
    
    @abstractmethod # Este método abstrato obriga que todas as classes que herdem Conta sejam obrigados a implementar passa_mes, evitando erros
    def passa_mes(self):
        pass

    def __str__(self):
        return f"Código {self.cod}\nSaldo: {self.saldo}"

class ContaCorrente(Conta):
    def passa_mes(self):
        self.saldo -= 2

class ContaPoupanca(Conta):
    def passa_mes(self):
        self.saldo *= 1.01
        self.saldo -= 3

class ContaInvestimento(Conta): # Dá erro ao instanciar por conta de não ter o passa_mes, obrigatório por conta do @abstractmethod
    pass

conta16 = ContaCorrente(16)
conta16.deposita(1000)
conta16.passa_mes()
print(conta16)

conta18 = ContaPoupanca(18)
conta18.deposita(1000)
conta18.passa_mes()
print(conta18)

contas = [conta16, conta18]

for conta in contas:
    conta.passa_mes() # Duck Typing
    print(conta)