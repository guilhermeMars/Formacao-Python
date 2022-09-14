class ContaCorrente:
    
    # Função construtora
    def __init__(self, numero, titular, saldo, limite = 1000.0): #Self é a referência do objeto na memória
        print("Construindo objeto... {}".format(self))
        self.__numero = numero
        self.__titular = titular    
        self.__saldo = saldo
        self.__limite = limite
    
    def extrato(self): # conta.extrato
        print("O saldo {} do titular {}".format(self.__saldo, self.__titular))

    def depositar(self, valor):
        self.__saldo += valor
    
    # Não é desejável que alguém use este método fora da classe
    def __pode_sacar(self, valor_saque):
        valor_a_sacar = self.saldo + self.limite
        return valor_saque <= valor_a_sacar

    def sacar(self, valor):
        if(self.__pode_sacar(valor)):
            self.__saldo -= valor
        else:
            print("O valor {} passou o limite".format(valor))

    def transferir(self, destino, valor):
        self.sacar(valor)
        destino.depositar(valor)

    @property
    def saldo(self):
        return self.__saldo

    @property
    def titular(self):
        return self.__titular

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, valor):
        self.__limite = valor
    
    # Métodos estáticos
    # Pois são da classe e não precisam de uma instância para funcionar
    @staticmethod # Conta.cod_banco()
    def cod_banco():
        return "001"




# class Data:
#     def __init__(self, dia, mes, ano):
#         self.dia = dia
#         self.mes = mes
#         self.ano = ano
    
#     def formata(self):
#         print("{}/{}/{}",format(self.dia, self.mes, self.ano))
