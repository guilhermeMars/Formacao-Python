## Dicionáio / Mapa
# Lista com chave e valor
# Parece muito com json

aparicoes = {
    "Guilherme" : 1,
    "cachorro" : 2,
    "nome" : 2,
    "vindo" : 1
}

# Outra forma, e bem menos comum, de declarar
aparicoes_dict = dict(Guilherme = 1, cachorro = 2)

guilherme = aparicoes["Guilherme"]
print(f"Aparição nome: {guilherme}")

# Caso não apareça, retorne 0
existe_ou_nao = aparicoes.get("Marianna", 0)
print(f"Não existe: {existe_ou_nao}")
existe_ou_nao = aparicoes.get("cachorro", 0)
print(f"Existe: {existe_ou_nao}")

# Adicionar um elemento
aparicoes["Carlos"] = 3
print(f"Adição carlos: {aparicoes}")

# Remover elemento
del aparicoes["Carlos"]
print(f"Removendo carlos: {aparicoes}")

# In
cachorro_in = "cachorro" in aparicoes
print(f"Cachorro está em aparições? {cachorro_in}")
um_in = 1 in aparicoes.values()
print(f"1 está nos valores? {um_in}")

# For
for elemento in aparicoes:
    #print(elemento)
    pass

# For pelas chaves
for elemento in aparicoes.keys():
    # print(elemento)
    pass

# For pelos values
for elemento in aparicoes.values():
    # print(elemento)
    pass

# For pelas duplas
# Muito comum
for chave, valor in aparicoes.items():
    print(f"{chave} - {valor}")
    pass
