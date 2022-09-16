# Regular Expression -- Regex
import re 
endereco = "Rua da Flores 72, apartamento 1002, Laranjeiras, Rio de Janeiro, RJ, 23440-120"

# Cep - 5 digitos + hífen (opcional) + 3 digitos

# Como funciona as expressões no python?
# Dentro dos [] são colocados os valores que podem aparecer
# Dentro das {} são colocados quantas vezes aquele padrão aparece
# Caso um valor possa ou não aparecer, é colocado um ? depois
padrao_cep = re.compile("[0-9]{5}[-]?[0-9]{3}")
busca = padrao_cep.search(endereco) # Match
if busca:
    cep = busca.group() #Retorna a string que foi encontrada
    print(f"Encontrou o cep!\n{cep}")
else:
    print("Cep não encontrado")


url = "https://bytebank.com/cambio?moedaDestino=dolar&quantidade=100&moedaOrigem=real"

# Parêntesis significa que o padrão precisa ser igual a
padrao_url = re.compile('(http[s]?://)?(www.)?bytebank.com(.br)?/cambio')
# Match vê se se encaixa no padrão apresentado
match_url = padrao_url.match(url)
if match_url:
    print("A url é valida!")
else:
    raise ValueError("A url NÃO é válida!")

