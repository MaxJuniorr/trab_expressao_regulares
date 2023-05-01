from src.arranjos_familiares import checa_arranjos_familiares
from src.common import gera_verificador
import pytest


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
# Casais heterossexuais mais velhos que os filhos, com a filha mais
# velha mulher e o filho mais novo homem.

def test_validar_arranjo_charlie_1() -> None:
    arranjo = "HHmmh"
    assert checa_arranjos_familiares.validar_arranjo_charlie(arranjo) == 0


def test_validar_arranjo_charlie_2() -> None:
    arranjo = "HmmhM"
    assert checa_arranjos_familiares.validar_arranjo_charlie(arranjo) == 0


def test_validar_arranjo_charlie_3() -> None:
    arranjo = "HMmhm"
    assert checa_arranjos_familiares.validar_arranjo_charlie(arranjo) == 0


def test_validar_arranjo_charlie_4() -> None:
    arranjo = "HMHmH"
    assert checa_arranjos_familiares.validar_arranjo_charlie(arranjo) == 0


def test_validar_arranjo_charlie_5() -> None:
    arranjo = "HMmhmh"
    assert checa_arranjos_familiares.validar_arranjo_charlie(arranjo)


def test_validar_arranjo_charlie_6() -> None:
    arranjo = "MHmmmmh"
    assert checa_arranjos_familiares.validar_arranjo_charlie(arranjo)


def test_validar_arranjo_charlie_7() -> None:
    arranjo = "HMmhhhhhhhhhhhhhhhhhhmhhhhhhhhhhhhhh"
    assert checa_arranjos_familiares.validar_arranjo_charlie(arranjo)


#### TESTES DELTA ####
# Casais heterossexuais mais velhos que os filhos, com pelo menos seis
# filhos, em que os dois primeiros filhos formam um casal e os ultimos
# também.

def test_validar_arranjo_delta_1() -> None:
    arranjo = "HMmhhmmh"
    assert checa_arranjos_familiares.validar_arranjo_delta(arranjo) == 0


def test_validar_arranjo_delta_2() -> None:
    arranjo = "HHmhmh"
    assert checa_arranjos_familiares.validar_arranjo_delta(arranjo) == 0


def test_validar_arranjo_delta_3() -> None:
    arranjo = "MMmhmhmm"
    assert checa_arranjos_familiares.validar_arranjo_delta(arranjo) == 0


def test_validar_arranjo_delta_4() -> None:
    arranjo = "HHhhmmmh"
    assert checa_arranjos_familiares.validar_arranjo_delta(arranjo) == 0


def test_validar_arranjo_delta_5() -> None:
    arranjo = "HHhmhhhhhhhhhmhmhmhmmhmhmhmm"
    assert checa_arranjos_familiares.validar_arranjo_delta(arranjo) == 0


def test_validar_arranjo_delta_6() -> None:
    arranjo = "MMhmhhm"
    assert checa_arranjos_familiares.validar_arranjo_delta(arranjo) == 0


def test_validar_arranjo_delta_7() -> None:
    arranjo = "HHmhhhhhhhhhhhhhhhhhhmhhhhhhhhhhhhhm"
    assert checa_arranjos_familiares.validar_arranjo_delta(arranjo)


def test_validar_arranjo_delta_8() -> None:
    arranjo = "MMmhmmmmmmmmmmmmhmhmh"
    assert checa_arranjos_familiares.validar_arranjo_delta(arranjo)


def test_validar_arranjo_delta_9() -> None:
    arranjo = "MMhmmhmh"
    assert checa_arranjos_familiares.validar_arranjo_delta(arranjo)

def test_validar_arranjo_delta_10() -> None:
    arranjo = "HHmhm"
    assert checa_arranjos_familiares.validar_arranjo_delta(arranjo) == 0

def test_validar_arranjo_delta_11() -> None:
    arranjo = "HHmhmhhh"
    assert checa_arranjos_familiares.validar_arranjo_delta(arranjo) == 0

#### TESTES ECHO ####
# Casais homossexuais mais velhos que os filhos, em que o sexo dos
# filhos é alternado conforme a ordem de nascimento.

def test_validar_arranjo_echo_1() -> None:
    arranjo = "HMm"
    assert checa_arranjos_familiares.validar_arranjo_echo(arranjo) == 0


def test_validar_arranjo_echo_2() -> None:
    arranjo = "MHmhm"
    assert checa_arranjos_familiares.validar_arranjo_echo(arranjo) == 0


def test_validar_arranjo_echo_3() -> None:
    arranjo = "HHmhhmh"
    assert checa_arranjos_familiares.validar_arranjo_echo(arranjo) == 0


def test_validar_arranjo_echo_4() -> None:
    arranjo = "MMm"
    assert checa_arranjos_familiares.validar_arranjo_echo(arranjo) 


def test_validar_arranjo_echo_5() -> None:
    arranjo = "HHhmhmhmhm"
    assert checa_arranjos_familiares.validar_arranjo_echo(arranjo)


def test_validar_arranjo_echo_6() -> None:
    arranjo = "MMhmhmhmhm"
    assert checa_arranjos_familiares.validar_arranjo_echo(arranjo)


def test_validar_arranjo_echo_7() -> None:
    arranjo = "HHmhmhm"
    assert checa_arranjos_familiares.validar_arranjo_echo(arranjo)


def test_validar_arranjo_echo_8() -> None:
    arranjo = "HHh"
    assert checa_arranjos_familiares.validar_arranjo_echo(arranjo)


def test_validar_arranjo_echo_9() -> None:
    arranjo = "MMh"
    assert checa_arranjos_familiares.validar_arranjo_echo(arranjo)


def test_validar_arranjo_echo_10() -> None:
    arranjo = "HHmhm"
    assert checa_arranjos_familiares.validar_arranjo_echo(arranjo)


#### TESTES FOXTROT ####
# Casais homossexuais mais velhos que os filhos, com qualquer quantidade
# de filhos homens e mulheres, mas que nâo tiveram dois filhos homens
# consecutivos

def test_validar_arranjo_foxtrot_1() -> None:
    arranjo = "HMm"
    assert checa_arranjos_familiares.\
        validar_arranjo_foxtrot(arranjo) == 0


def test_validar_arranjo_foxtrot_2() -> None:
    arranjo = "HHhh"
    assert checa_arranjos_familiares.\
        validar_arranjo_foxtrot(arranjo) == 0


def test_validar_arranjo_foxtrot_3() -> None:
    arranjo = "MMmhhm"
    assert checa_arranjos_familiares.\
        validar_arranjo_foxtrot(arranjo) == 0


def test_validar_arranjo_foxtrot_4() -> None:
    arranjo = "HH"
    assert checa_arranjos_familiares.\
        validar_arranjo_foxtrot(arranjo)


def test_validar_arranjo_foxtrot_5() -> None:
    arranjo = "MM"
    assert checa_arranjos_familiares.\
        validar_arranjo_foxtrot(arranjo)


def test_validar_arranjo_foxtrot_6() -> None:
    arranjo = "HHhmmhmhmmh"
    assert checa_arranjos_familiares.\
        validar_arranjo_foxtrot(arranjo)


def test_validar_arranjo_foxtrot_7() -> None:
    arranjo = "HHhmh"
    assert checa_arranjos_familiares.\
        validar_arranjo_foxtrot(arranjo)


#### TESTES GOLF ####
# Arranjo de no minimo x∈N e no maximo y∈N, com x>0, y>0, e x<=y, de
# adultos (Hs ou Ms) mais velhos que os filhos, com qualquer quantidade
# de filhos homens e mulheres, mas que os três filhos mais novos não
# foram homens.

def test_validar_arranjo_golf_1() -> None:
    """Teste quando x > y"""
    x = 3
    y = 2
    arranjo = "HHHMMhmhmhmhm"
    with pytest.raises(Exception) as e:
        checa_arranjos_familiares.validar_arranjo_golf(arranjo, x, y)
        assert str(e.value) == "Os parâmetros não obedecem a regra x > 0, y > 0 , e x <= y"


def test_validar_arranjo_golf_2() -> None:
    """Teste quando x == 0"""
    x = 0
    y = 10
    arranjo = "HHHMMMhhmh"
    with pytest.raises(Exception) as e:
        checa_arranjos_familiares.validar_arranjo_golf(arranjo, x, y)
        assert str(e.value) == "Os parâmetros não obedecem a regra x > 0, y > 0 , e x <= y"


def test_validar_arranjo_golf_3() -> None:
    """Teste quando numero de pais not in range(2,5)"""
    x = 2
    y = 5
    arranjo = "HHHMMMhmmhmh"
    assert checa_arranjos_familiares.validar_arranjo_golf(arranjo, x, y) == 0


def test_validar_arranjo_golf_4() -> None:
    x = 2
    y = 3
    arranjo = "HHHMMMhh"
    assert checa_arranjos_familiares.validar_arranjo_golf(arranjo, x, y) == 0


def test_validar_arranjo_golf_5() -> None:
    x = 3
    y = 5
    arranjo = "HHhhhm"
    assert checa_arranjos_familiares.validar_arranjo_golf(arranjo, x, y) == 0


def test_validar_arranjo_golf_6() -> None:
    x = 1
    y = 3
    arranjo = "HMmhmhmhmmhhh"
    assert checa_arranjos_familiares.validar_arranjo_golf(arranjo, x, y) == 0


def test_validar_arranjo_golf_7() -> None:
    x = 1
    y = 3
    arranjo = "HM"
    assert checa_arranjos_familiares.validar_arranjo_golf(arranjo, x, y)


def test_validar_arranjo_golf_8() -> None:
    x = 3
    y = 5
    arranjo = "HMMmhmhmhmmhhmhh"
    assert checa_arranjos_familiares.validar_arranjo_golf(arranjo, x, y)


def test_validar_arranjo_golf_9() -> None:
    x = 2
    y = 4
    arranjo = "HHHMhhhmh"
    assert checa_arranjos_familiares.validar_arranjo_golf(arranjo, x, y)


def test_validar_arranjo_golf_10() -> None:
    x = 7
    y = 7
    arranjo = "HHHMMHMhhhmhh"
    assert checa_arranjos_familiares.validar_arranjo_golf(arranjo, x, y)


def test_validar_arranjo_golf_11() -> None:
    x = 1
    y = 1
    arranjo = "HMHHMhmhm"
    assert checa_arranjos_familiares.validar_arranjo_golf(arranjo, x, y) == 0


def test_validar_arranjo_golf_12() -> None:
    x = 1
    y = 1
    arranjo = "H"
    assert checa_arranjos_familiares.validar_arranjo_golf(arranjo, x, y)
