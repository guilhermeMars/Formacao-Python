import requests


class BuscaEndereco:
    def __init__(self, cep):
        cep = str(cep)
        if self.validar_cep(cep):
            self.cep = cep
        else:
            raise ValueError("Cep inválido!")

    def __str__(self):
        return "{}-{}".format(self.cep[:5], self.cep[5:])

    def validar_cep(self, cep):
        if len(cep) == 8:
            return True
        else:
            return False
    
    def acessa_por_cep(self):
        url = "https://viacep.com.br/ws/{}/json".format(self.cep)
        req = requests.get(url)
        dados = req.json()
        return(
            dados['bairro'],
            dados['localidade'],
            dados['uf']
        )
