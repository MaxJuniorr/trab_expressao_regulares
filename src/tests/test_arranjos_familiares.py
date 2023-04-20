from src.checa_arranjos_familiares import checa_arranjos_familiares
from src.common import helper


def test_validar_arranjo_alfa_1() -> None:
    nome = "HMm"
    assert checa_arranjos_familiares.validar_caso_alfa(nome) == 0


def test_validar_arranjo_alfa_2() -> None:
    nome = "mH"
    assert checa_arranjos_familiares.validar_caso_alfa(nome) == 0


def test_validar_arranjo_alfa_3() -> None:
    nome = "HH"
    assert checa_arranjos_familiares.validar_caso_alfa(nome) == 0

def test_validar_arranjo_alfa_4() -> None:
    nome = "MM"
    assert checa_arranjos_familiares.validar_caso_alfa(nome) == 0
