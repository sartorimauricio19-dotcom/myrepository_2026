import pytest
from calc2 import sumar, restar, multiplicar, dividir

# Fixture de enteros existente
@pytest.fixture
def numeros_enteros():
    return 10, 5

# Segundo fixture con valores flotantes pedido en la actividad[cite: 6]
@pytest.fixture
def numeros_flotantes():
    return 0.1, 0.2

# 1- Pruebas para SUMAR (Éxito y flotantes)[cite: 6]
def test_sumar_exito(numeros_enteros):
    a, b = numeros_enteros
    assert sumar(a, b) == 15

def test_sumar_flotantes(numeros_flotantes):
    a, b = numeros_flotantes
    assert pytest.approx(sumar(a, b)) == 0.3

# 1- Pruebas para RESTAR (Éxito y error/negativos)[cite: 6]
def test_restar_exito(numeros_enteros):
    a, b = numeros_enteros
    assert restar(a, b) == 5

def test_restar_error():
    assert restar(5, 10) == -5

# 1- Pruebas para MULTIPLICAR (Éxito y cero)[cite: 6]
def test_multiplicar_exito(numeros_enteros):
    a, b = numeros_enteros
    assert multiplicar(a, b) == 50

def test_multiplicar_por_cero():
    assert multiplicar(10, 0) == 0

# 1- Pruebas para DIVIDIR (Éxito y control de error por cero)[cite: 6]
def test_dividir_exito(numeros_enteros):
    a, b = numeros_enteros
    assert dividir(a, b) == 2.0

def test_dividir_por_cero():
    with pytest.raises(ValueError):
        dividir(10, 0)