from funcionario import Funcionario
import pytest
from pytest import mark


class TestClass:
    def test_quando_idade_recebe_13_03_2000_deve_retornar_22(self):
        entrada = "13/03/2000"  # Given - Contexto
        esperado = 22

        funcionario_teste = Funcionario("Teste", entrada, 1111)
        resultado = funcionario_teste.idade() # When-ação

        assert resultado == esperado # Then-desfecho

    def test_quando_sobrenome_recebe_Felipe_Rodrigues_deve_retornar_Rodrigues(self):
        entrada = " Felipe Rodrigues " #Given - Contexto
        esperado = "Rodrigues"

        lucas = Funcionario(entrada, "11/11/2000", 1111)
        resultado = lucas.sobrenome() # When - Ação

        assert resultado == esperado

    def test_quando_decrescimo_salario_recebe_100000_deve_retornar_90000(self):
        entrada = 100000 #Given - Contexto
        entrada_nome = "Felipe Bragança"
        esperado = 90000


        funcionario_teste = Funcionario(entrada_nome, 11/11/2000, entrada)
        funcionario_teste.decrescimo_salario() 
        resultado = funcionario_teste.salario  # When - Ação

        assert resultado == esperado  #then 
    
    @mark.calcular_bonus
    def test_quando_calcular_bonus_recebe_1000_deve_retornar_100(self):
        entrada = 1000 #Given - Contexto
        esperado = 100


        funcionario_teste = Funcionario("Teste", 11/11/2000, entrada) 
        resultado = funcionario_teste.calcular_bonus()  # When - Ação

        assert resultado == esperado  #then 
    @mark.calcular_bonus
    def test_quando_calcular_quando_recebe_1000000_deve_retornar_exception(self):
        with pytest.raises(Exception):
            entrada = 1000000 #Given - Contexto
        

            funcionario_teste = Funcionario(entrada_nome, 11/11/2000, entrada)

            resultado = funcionario_teste.calcular_bonus()  # When - Ação

            assert resultado # then