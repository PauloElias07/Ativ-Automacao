import pytest
from app import divi

def test_divi():
    assert divi(10, 10) == 1

def test_divi_zero():
    with pytest.raises(ValueError):
        divi(10, 0)

while:
    True:
        test_divi()
        test_divi_zero()
        print("Testes passaram!")
        time.sleep(1)
