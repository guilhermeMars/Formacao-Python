## Igualdade com __eq__

class ContaSalario():
    def __init__(self, cod):
        self.cod = cod
        self.saldo = 0
    
    def deposita(self, valor):
        self.saldo += valor

    def __str__(self):
        return f"Código {self.cod}\nSaldo: {self.saldo}"
    
    def __eq__(self, eq):
        # Verifica se é do mesmo tipo ou se não é uma instância (opcional)
        if type(eq) != ContaSalario or not isinstance(ContaSalario, type(eq)):
            return False
        # Pode-se comparar o saldo também, com: and self.saldo == eq.saldo
        return self.cod == eq.cod 

conta1 = ContaSalario(37)
conta2 = ContaSalario(37)
print(f"As contas são iguais? {conta1 == conta2}")