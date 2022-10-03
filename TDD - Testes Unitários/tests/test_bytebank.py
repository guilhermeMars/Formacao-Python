# pip install pytest==7.1.2
# A pasta precisa ter o nome tests

from codigo.bytebank import Funcionario
from pytest import pytest, mark

class TestClass:
    # Para o pytest reconhecer que é um teste
    # Precisa começar com test_
    # Nome bem explicativo
    def test_quando_idade_recebe_07_07_2004_deve_retornar_18(self):
        # Given (contexto)
        entrada = '07/07/2004'
        esperado = 18
        
        funcionario_teste = Funcionario('Teste', entrada, 1111)
        # When (Ação)
        resultado = funcionario_teste.idade()

        #Then (desfecho)
        assert resultado == esperado
    
    def test_quando_sobrenome_recebe_Guilherme_Martins_retorna_Martins(self):
        entrada = 'Guilherme Martins' # Given
        esperado = 'Martins'

        guilherme = Funcionario(entrada, '11/11/2000', 1111)
        resultado = guilherme.sobrenome() # When

        assert resultado == esperado # Then
    
    # TDD - Test Drive Development (Desenvolvimento Guiado por Testes)
    # Cria os testes primeiro, depois o código
    # Aplica as regras de negócio no teste e faz com que o código passe

    @mark.calcular_bonus
    def test_quando_decrescimo_salario_recebe_100000_retorna_90000(self):
        entrada_salario = 100000 # GIven
        entrada_nome = 'Paulo Bragança'
        esperado = 90000

        funcionario_teste = Funcionario(entrada_nome, '11/11/2000', entrada_salario)
        funcionario_teste.decrescimo_salario() # When
        resultado = funcionario_teste.salario

        assert resultado == esperado # Then
    
    # (Terminal) pytest --markers
    @mark.calcular_bonus
    def test_quando_calcular_bonus_recebe_100000000_retorna_exception(self):
        # Faz com que o pytest já espere uma Exeption
        with pytest.raises(Exception):
            entrada = 100000000  # given

            funconario_teste = Funcionario('teste', '11/11/2000', entrada)
            resultado = funconario_teste.calcular_bonus()  # when

            assert resultado  # then

# pytest.ini - Arquivo de configuração do pytest. Dá prioridade para as configurações digitadas no mesmo

# python -m pytest
