import pytest
from calc2 import sumar, restar, multiplicar, dividir

# Fixture de enteros
@pytest.fixture
def numeros_enteros():
    return 10, 5

# Fixture con valores flotantes
@pytest.fixture
def numeros_flotantes():
    return 0.1, 0.2

# Parametrización para SUMAR con 3 datasets y marcador smoke
@pytest.mark.smoke
@pytest.mark.parametrize("a, b, resultado_esperado", [
    (2, 3, 5),
    (10, 20, 30),
    (-5, 5, 0)
])
def test_sumar_parametrizado(a, b, resultado_esperado):
    assert sumar(a, b) == resultado_esperado

def test_sumar_flotantes(numeros_flotantes):
    a, b = numeros_flotantes
    assert pytest.approx(sumar(a, b)) == 0.3

# Parametrización para RESTAR con 3 datasets
@pytest.mark.parametrize("a, b, resultado_esperado", [
    (10, 5, 5),
    (5, 10, -5),
    (0, 0, 0)
])
def test_restar_parametrizado(a, b, resultado_esperado):
    assert restar(a, b) == resultado_esperado

# Pruebas para MULTIPLICAR
def test_multiplicar_exito(numeros_enteros):
    a, b = numeros_enteros
    assert multiplicar(a, b) == 50

def test_multiplicar_por_cero():
    assert multiplicar(10, 0) == 0

# Pruebas para DIVIDIR
def test_dividir_exito(numeros_enteros):
    a, b = numeros_enteros
    assert dividir(a, b) == 2.0

# Marcador exception para el test que valida la división por cero
@pytest.mark.exception
def test_dividir_por_cero():
    with pytest.raises(ValueError):
        dividir(10, 0)