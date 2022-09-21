from audioop import reverse
from wsgiref.validate import validator


idades = [15, 87, 65, 56, 23, 48, 33]

# for i in range(len(idades)):
#     print(i, idades[i])

## Enumerate - pega e posição e o valor em uma lista
numeros = list(enumerate(idades))
print(numeros)
for indice, idade in enumerate(idades):
    print(f"Indice: {indice} - Valor: {idade}")

## Desenpacotar
usuarios = [
    ('Guilherme Martins', 18, 2004),
    ('Daniela', 24, 1998),
    ('Marcos', 32, 1990)
]

for nome, idade, ano in usuarios:
    print(nome)

# O _ mosta que o valor não será utilizado e não precisa ser desempacotado
for nome, _, _ in usuarios:
    print(nome)

## Sorted
ordenado = sorted(idades) # Mantém ordenada as idades
print(ordenado)
ordenado_contrario = sorted(idades, reverse=True) # É possível ver este atributo na documentação
print(ordenado_contrario)
## Já ordena a própria lista
# idades.sort() 

## Reversed
reverso = list(reversed(idades)) # Coloca a lista ao contrário
print(reverso)

c = "a" < "b"
print(c)
