from cpf_cnpj import Documento
from telefones_br import TelefonesBr
from datas_br import DatasBr
from acesso_cep import BuscaEndereco
import requests


cpf = str(15316264754)
documento_cpf = Documento.cria_documento(cpf)
print(f"Documento cpf: {documento_cpf}")

cnpj = str(35379838000112)
documento_cnpj = Documento.cria_documento(cnpj)
print(f"Documento cnpj: {documento_cnpj}")

telefone = "551999007601"
telefone_obj = TelefonesBr(telefone)
print(f"Objeto telefone: {telefone_obj}")

cadastro = DatasBr()
print(f"Cadastro de datas: {cadastro}")

url = "https://viacep.com.br/ws/13013160/json"
req = requests.get(url)
print(f"Tipo do text: {type(req.text)}")
print(f"Tipo do json(): {type(req.json())}")
print(f"Todos os dados: {req.json()}")
print(f"Apenas o bairro: {req.json()['bairro']}")

cep = 13013160
objeto_cep = BuscaEndereco(cep)
bairro, cidade, uf = objeto_cep.acessa_por_cep()
print(bairro, cidade, uf)



# Primeira classe

# from cpf_cnpj import CpfCnpj
# cpf = str(15316264754)
# objeto_cpf = CpfCnpj(cpf, "cpf")
# cnpj = str(35379838000112)
# objeto_cnpj = CpfCnpj(cnpj, "cnpj")

# print(objeto_cpf)
# print(objeto_cnpj)