class Cliente:
    
    def __init__(self, nome):
        self.__nome = nome

    @property 
    def nome(self): # cliente.nome
        print("Chamando @property nome")
        return self.__nome.title() # Deixa em maiúsculo
    
    @nome.setter
    def nome(self, nome):
        print("Chamando @setter nome")
        self.__nome = nome