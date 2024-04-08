# bibliotecas, frameworks e referencias externas
import pytest
from utils.utils import read_csv
from calculadora import somar_dois_numeros, subtrair_dois_numeros, multiplicar_dois_numeros, dividir_dois_numeros

# testes
#Padrão /Standard AAA (se diz tiple A/ 3A) = Arrange(Prepara, Configura - Dados de entrada e saída), Act(executa), Assert(Valida)

#Preparar
@pytest.mark.parametrize('num1, num2, resultado_esperado',
                        [ #array/matriz
                            (5, 7, 12), #tupla/registro
                            (0, 8, 8),
                            (10, -15, -5),
                            (6, 0.75, 6.75)
                        ])

def test_somar_dois_numeros(num1, num2, resultado_esperado):

    #Executar
    resultado_obtido = somar_dois_numeros(num1, num2);

    #Validar
    assert resultado_esperado == resultado_obtido



