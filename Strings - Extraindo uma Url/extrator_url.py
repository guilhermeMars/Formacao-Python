import re

class ExtratorUrl:
    def __init__(self, url):
        self.url = self.sanitiza_url(url)
        self.valida_url()
    
    def sanitiza_url(self, url):
        if type(url) == str:
            return url.strip()
        else:
            return "None"
    
    def valida_url(self):
        if self.url == "":
            raise ValueError("A url está vazia") # Enviar um erro de valor
        else:
            padrao_url = re.compile('(http[s]?://)?(www.)?bytebank.com(.br)?/cambio')
            match_url = padrao_url.match(self.url)
            if match_url:
                print("A url é valida!")
            else:
                raise ValueError("A url NÃO é válida!")

    def get_url_base(self):
        index_interrogacao = self.url.find("?")
        return self.url[0:index_interrogacao]

    def get_url_params(self):
        index_interrogacao = self.url.find("?")
        return self.url[index_interrogacao+1:]
    
    def get_valor_params(self, nome_param):
        params_url = self.get_url_params()
        index_params = params_url.find(nome_param)

        index_valor = index_params + len(nome_param) + 1
        index_ecomercial = params_url.find("&", index_valor)
        if index_ecomercial == -1:
            return params_url[index_valor:]
        else:
            return params_url[index_valor:index_ecomercial]

    def __len__(self):
        return len(self.url)
    
    def __str__(self):
        return f"A url utilizada é {self.url}\nE seus parâmetros são {self.get_url_params()}"

    def __eq__(self, other):
        return self.url == other.url


url1 = ExtratorUrl("https://bytebank.com/cambio?moedaDestino=dolar&quantidade=100&moedaOrigem=real")
print(url1)
valor_quantidade = url1.get_valor_params("quantidade")
print(valor_quantidade)

valor_dolar = 5.50
moeda_origem = url1.get_valor_params('moedaOrigem')
moeda_destino = url1.get_valor_params('moedaDestino')
quantidade = int(url1.get_valor_params('quantidade'))

if moeda_origem == 'real' and moeda_destino == 'dolar':
    valor_conversao = quantidade * valor_dolar
    print(f"O valor da conversão de real para dólar foi {str(valor_conversao)}")
elif moeda_origem == 'dolar' and moeda_destino == 'real':
    valor_conversao = quantidade / valor_dolar
    print(f"O valor da conversão de dólar para real foi {str(valor_conversao)}")
else:
    print("Os valores digitados não correspondem ao de real e dólar!")