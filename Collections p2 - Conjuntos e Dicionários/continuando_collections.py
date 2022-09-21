usuarios_data_science = [15, 23, 43, 56]
usuarios_machine_learning = [13, 23, 56, 42]

## Copy
# Faz uma cópia "raza"
# Caso tenham objetos ele não cria outro objeto, apenas copia a referência
assistiram = usuarios_data_science.copy()
assistiram.extend(usuarios_machine_learning)
print(f"Cópia e extend: {assistiram}")

## Set / Conjunto
# Ignora e não adiciona números repetidos
# É mutável
# A ordem não importa, não é possível acessar o elemento
# assistiram_email[2] # Não funciona
assistiram_email = set(assistiram)
print(f"Set / Conjunto: {assistiram_email}")
# Pode ser usado o {}
teste_conjunto1 = {1, 2, 3, 1, 2}
teste_conjunto2 = {3, 4, 5, 6, 1}
print(f"Teste conjunto: {teste_conjunto1}")

# Forma de juntar os conjuntos
juntando_testes = teste_conjunto1 | teste_conjunto2
print(f"Juntando: {juntando_testes}")

# Forma de pegar a intersecção entre os elementos
intersecção_testes = teste_conjunto1 & teste_conjunto2
print(f"Intersecção: {intersecção_testes}")

# Pega quem está em 1 mas não no 2
subtracao_testes = teste_conjunto1 - teste_conjunto2
print(f"Subtração: {subtracao_testes}")

# Ou exclusivo - Fez um ou outro, não os dois
exclusivo_testes = teste_conjunto1 ^ teste_conjunto2
print(f"Exclusivo: {exclusivo_testes}")

# Mutabilidade do Conjunto
teste_conjunto2.add(7)
print(f"Len / Tamanho: {len(teste_conjunto2)}")

# Parar a mutabilidade
teste_conjunto3 = frozenset(teste_conjunto2)
print(f"Frozenset tipo: {type(teste_conjunto3)}")

# Funciona com strings
frase = "Bem vindo meu nome é Guilherme eu gosto muito de nomes e tenho o meu cachorro e gosto muito de cachorro"
frase_sem_espaco = frase.split()
frase_conjunto = set(frase_sem_espaco) # Pega todas as palavras do texto
print(f"Conjunto frase: {frase_conjunto}")


# for assistiram in assistiram_email:
#     print(f"For: {assistiram}")