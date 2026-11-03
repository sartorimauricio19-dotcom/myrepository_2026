import pytest
from calc import sumar, dividir 


def test_sumar_positivo():
  assert sumar(2, 3) == 5


def test_dividir_por_zero():
  with pytest.raises(ValueError):
    dividir(1, 0)