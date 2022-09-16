url = "https://bytebank.com/cambio?moedaDestino=dolar&quantidade=100&moedaOrigem=real"

#Sanitização (limpeza) da url
# url = url .replace(" ", "")
url = url .strip()

#Validação da url
if url == "":
    raise ValueError("A url está vazia") # Enviar um erro de valor
elif "http" in url or "https" in url:
    print("Passou no teste")
else:
    raise ValueError("Houve um erro")

# Separa a base e os params
index_interrogacao = url.find("?")

base_url = url[0:index_interrogacao]

params_url = url[index_interrogacao+1:]

# Busca o valor do params
params_busca = 'moedaOrigem'
index_params = params_url.find(params_busca)

index_valor = index_params + len(params_busca) + 1
index_ecomercial = params_url.find("&", index_valor)
if index_ecomercial == -1:
    valor = params_url[index_valor:]
else:
    valor = params_url[index_valor:index_ecomercial]
print(valor)



# base_url = url[0:19]

# print(base_url)

# params_url = url[20:36]

# print(params_url)