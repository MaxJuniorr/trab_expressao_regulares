from src.checa_arranjos_familiares import checa_arranjos_familiares
from src.common import helper


#### TESTES ALFA ####
def test_validar_arranjo_alfa_1() -> None:
    arranjo = "HMm"
    assert checa_arranjos_familiares.validar_arranjo_alfa(arranjo) == 0


def test_validar_arranjo_alfa_2() -> None:
    arranjo = "mH"
    assert checa_arranjos_familiares.validar_arranjo_alfa(arranjo) == 0


def test_validar_arranjo_alfa_3() -> None:
    arranjo = "HH"
    assert checa_arranjos_familiares.validar_arranjo_alfa(arranjo) == 0


def test_validar_arranjo_alfa_4() -> None:
    arranjo = "MM"
    assert checa_arranjos_familiares.validar_arranjo_alfa(arranjo) == 0


def test_validar_arranjo_alfa_5() -> None:
    arranjo = "HMmm"
    assert checa_arranjos_familiares.validar_arranjo_alfa(arranjo)


def test_validar_arranjo_alfa_6() -> None:
    arranjo = "HMh"
    assert checa_arranjos_familiares.validar_arranjo_alfa(arranjo)


def test_validar_arranjo_alfa_7() -> None:
    arranjo = "HMhhhhmhhhm"
    assert checa_arranjos_familiares.validar_arranjo_alfa(arranjo)


def test_validar_arranjo_alfa_8() -> None:
    arranjo = "MHmhhhhhhhhhhhhh"
    assert checa_arranjos_familiares.validar_arranjo_alfa(arranjo)


def test_validar_arranjo_alfa_9() -> None:
    arranjo = "MHhhhhhhmhhhhhhh"
    assert checa_arranjos_familiares.validar_arranjo_alfa(arranjo)


def test_validar_arranjo_alfa_10() -> None:
    arranjo = "MHhhhhhhhhhhhhhm"
    assert checa_arranjos_familiares.validar_arranjo_alfa(arranjo)


#### TESTES BETA ####
def test_validar_arranjo_beta_1() -> None:
    arranjo = "HMmmh"
    assert checa_arranjos_familiares.validar_arranjo_beta(arranjo) == 0


def test_validar_arranjo_beta_2() -> None:
    arranjo = "mmmhHM"
    assert checa_arranjos_familiares.validar_arranjo_beta(arranjo) == 0


def test_validar_arranjo_beta_3() -> None:
    arranjo = "HHmmm"
    assert checa_arranjos_familiares.validar_arranjo_beta(arranjo) == 0


def test_validar_arranjo_beta_4() -> None:
    arranjo = "MH"
    assert checa_arranjos_familiares.validar_arranjo_beta(arranjo) == 0


def test_validar_arranjo_beta_5() -> None:
    arranjo = "HMhmmhmh"
    assert checa_arranjos_familiares.validar_arranjo_beta(arranjo)

def test_validar_arranjo_beta_6() -> None:
    arranjo = "MHmh"
    assert checa_arranjos_familiares.validar_arranjo_beta(arranjo)


def test_validar_arranjo_beta_7() -> None:
    arranjo = "HMhhhhhhhmhmhhhhhhhmhhhhhhhhhhhhhh"
    assert checa_arranjos_familiares.validar_arranjo_beta(arranjo)


def test_validar_arranjo_beta_8() -> None:
    arranjo = "MHhhhhhhhhhhhhhhhhhhhmhhhhhhh"
    assert checa_arranjos_familiares.validar_arranjo_beta(arranjo)


#### TESTES CHARLIE ####

