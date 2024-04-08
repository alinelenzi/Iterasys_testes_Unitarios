# bibliotecas, frameworks e referencias externas
import pytest
from utils.utils import read_csv
from calculadora import somar_dois_numeros, subtrair_dois_numeros, multiplicar_dois_numeros, dividir_dois_numeros

# testes
#Padrão /Standard AAA (se diz tiple A/ 3A) = Arrange(Prepara, Configura - Dados de entrada e saída), Act(executa), Assert(Valida)

#Preparar
@pytest.mark.parametrize('num1, num2, resultado_esperado', read_csv('./fixtures/massa_somar.csv'))

def test_somar_dois_numeros_csv(num1, num2, resultado_esperado):

    #Executar
    resultado_obtido = somar_dois_numeros(float (num1), float(num2));

    #Validar
    assert float(resultado_esperado) == resultado_obtido
