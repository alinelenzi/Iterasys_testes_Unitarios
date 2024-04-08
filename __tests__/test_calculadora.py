# bibliotecas, frameworks e referencias externas
import pytest
from calculadora import somar_dois_numeros, subtrair_dois_numeros, multiplicar_dois_numeros, dividir_dois_numeros

# testes
#Padrão /Standard AAA (se diz tiple A/ 3A) = Arrange(Prepara, Configura - Dados de entrada e saída), Act(executa), Assert(Valida)

def test_somar_dois_numeros():
    #Preparar
    num1 = 5;
    num2 = 7;
    resultado_esperado = 12;

    #Executar
    resultado_obtido = somar_dois_numeros(num1, num2);

    #Validar
    assert resultado_esperado == resultado_obtido

def test_subtrair_dois_numeros():
    num1 = 7;
    num2 = 5;
    resultado_esperado = 2;

    #Executar
    resultado_obtido = subtrair_dois_numeros(num1, num2);

    #Validar
    assert resultado_esperado == resultado_obtido

def test_multiplicar_dois_numeros():
    num1 = 5;
    num2 = 7;
    resultado_esperado = 35;

    #Executar
    resultado_obtido = multiplicar_dois_numeros(num1, num2);

    #Validar
    assert resultado_esperado == resultado_obtido

def test_dividir_dois_numeros():
    num1 = 35;
    num2 = 7;
    resultado_esperado = 5;

    #Executar
    resultado_obtido = dividir_dois_numeros(num1, num2);

    #Validar
    assert resultado_esperado == resultado_obtido

def test_dividir_por_zero():
    num1 = 35;
    num2 = 0;
    resultado_esperado = "Erro: Não é possível dividir por zero.";

    #Executar
    resultado_obtido = dividir_dois_numeros(num1, num2);

    #Validar
    assert resultado_esperado == resultado_obtido



