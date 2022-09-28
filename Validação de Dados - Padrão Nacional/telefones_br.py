import re
from urllib import response

class TelefonesBr:
    def __init__(self, telefone):
        if self.valida_telefone(telefone):
            self.telefone = telefone
        else:
            raise ValueError("Numero incorreto!!!")

    def __str__(self):
        return self.format_numero()

    def valida_telefone(self, telefone):
        # https://cursos.alura.com.br/forum/topico-o-codigo-da-erro-no-telefone-de-nove-digitos-resolvido-234650
        padrao = "([0-9]{2,3}?)?([1-9]{2})([6-9])?([0-9]{4})([0-9]{4}$)"
        resposta = re.findall(padrao, telefone)
        if resposta:
            return True
        else:
            return False
    
    def format_numero(self):
        padrao = "([0-9]{2,3})?([0-9]{2})([0-9]{4,5})([0-9]{4})"
        resposta = re.search(padrao, self.telefone)
        # if not resposta.group():
        #     resposta.group() = 55
        return "+{} ({}) {}-{}".format(resposta.group(1), resposta.group(2), resposta.group(3), resposta.group(4))
