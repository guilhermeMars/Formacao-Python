import re

padrao = "[0-9][a-z][0-9]"
texto = "123 1a2 1cc aa1"
resposta = re.search(padrao, texto) # Search pega apenas a primeira ocorrência
print(resposta)
print(resposta.group())

padrao_email = "\w{5,50}@\w{3,10}.\w{2,3}(.\w{2,3})?"
texto_email = "aaabbbccc guilhermemspiandorin321@gmail.com"
resposta_email = re.search(padrao_email, texto_email)
print(resposta_email.group())

padrao_telefone = "[0-9]{2}[0-9]{4,5}[0-9]{4}"
texto_telefone = "gosto no numero 19999007601 e do 2126451234"
resposta_telefone = re.findall(padrao_telefone, texto_telefone)
print(resposta_telefone)
