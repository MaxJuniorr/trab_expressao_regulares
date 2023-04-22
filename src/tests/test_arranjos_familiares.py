from src.checa_arranjos_familiares import checa_arranjos_familiares
from src.common import helper


alfa = checa_arranjos_familiares.Alfa()
verif_alfa = helper.Verificador(alfa)

beta = checa_arranjos_familiares.Beta()
verif_beta = helper.Verificador(beta)

charlie = checa_arranjos_familiares.Charlie()
verif_charlie = helper.Verificador(charlie)

delta = checa_arranjos_familiares.Delta()
verif_delta = helper.Verificador(delta)

echo = checa_arranjos_familiares.Echo()
verif_echo = helper.Verificador(echo)

foxtrot = checa_arranjos_familiares.Foxtrot()
verif_foxtrot = helper.Verificador(foxtrot)

golf = checa_arranjos_familiares.Golf()
verif_golf = helper.Verificador(golf)


#### TESTES ALFA ####
def test_validar_arranjo_alfa_1() -> None:
    arranjo = "HMm"
    assert verif_alfa.reconhecer(arranjo) == 0


def test_validar_arranjo_alfa_2() -> None:
    arranjo = "mH"
    assert verif_alfa.reconhecer(arranjo) == 0


def test_validar_arranjo_alfa_3() -> None:
    arranjo = "HH"
    assert verif_alfa.reconhecer(arranjo) == 0


def test_validar_arranjo_alfa_4() -> None:
    arranjo = "MM"
    assert verif_alfa.reconhecer(arranjo) == 0


def test_validar_arranjo_alfa_5() -> None:
    arranjo = "HMmm"
    assert verif_alfa.reconhecer(arranjo)


def test_validar_arranjo_alfa_6() -> None:
    arranjo = "HMh"
    assert verif_alfa.reconhecer(arranjo)


def test_validar_arranjo_alfa_7() -> None:
    arranjo = "HMhhhhmhhhm"
    assert verif_alfa.reconhecer(arranjo)


def test_validar_arranjo_alfa_8() -> None:
    arranjo = "MHmhhhhhhhhhhhhh"
    assert verif_alfa.reconhecer(arranjo)


def test_validar_arranjo_alfa_9() -> None:
    arranjo = "MHhhhhhhmhhhhhhh"
    assert verif_alfa.reconhecer(arranjo)


def test_validar_arranjo_alfa_10() -> None:
    arranjo = "MHhhhhhhhhhhhhhm"
    assert verif_alfa.reconhecer(arranjo)


#### TESTES BETA ####
def test_validar_arranjo_beta_1() -> None:
    arranjo = "HMmmh"
    assert verif_beta.reconhecer(arranjo) == 0


def test_validar_arranjo_beta_2() -> None:
    arranjo = "mmmhHM"
    assert verif_beta.reconhecer(arranjo) == 0


def test_validar_arranjo_beta_3() -> None:
    arranjo = "HHmmm"
    assert verif_beta.reconhecer(arranjo) == 0


def test_validar_arranjo_beta_4() -> None:
    arranjo = "MH"
    assert verif_beta.reconhecer(arranjo) == 0


def test_validar_arranjo_beta_5() -> None:
    arranjo = "HMhmmhmh"
    assert verif_beta.reconhecer(arranjo)


def test_validar_arranjo_beta_6() -> None:
    arranjo = "MHmh"
    assert verif_beta.reconhecer(arranjo)


def test_validar_arranjo_beta_7() -> None:
    arranjo = "HMhhhhhhhmhmhhhhhhhmhhhhhhhhhhhhhh"
    assert verif_beta.reconhecer(arranjo)


def test_validar_arranjo_beta_8() -> None:
    arranjo = "MHhhhhhhhhhhhhhhhhhhhmhhhhhhh"
    assert verif_beta.reconhecer(arranjo)


#### TESTES CHARLIE ####
# Casais heterossexuais mais velhos que os filhos, com a filha mais
# velha mulher e o filho mais novo homem.

def test_validar_arranjo_charlie_1() -> None:
    arranjo = "HHmmh"
    assert verif_charlie.reconhecer(arranjo) == 0


def test_validar_arranjo_charlie_2() -> None:
    arranjo = "HmmhM"
    assert verif_charlie.reconhecer(arranjo) == 0


def test_validar_arranjo_charlie_3() -> None:
    arranjo = "HMmhm"
    assert verif_charlie.reconhecer(arranjo) == 0


def test_validar_arranjo_charlie_4() -> None:
    arranjo = "HMHmH"
    assert verif_charlie.reconhecer(arranjo) == 0


def test_validar_arranjo_charlie_5() -> None:
    arranjo = "HMmhmh"
    assert verif_charlie.reconhecer(arranjo)


def test_validar_arranjo_charlie_6() -> None:
    arranjo = "MHmmmmh"
    assert verif_charlie.reconhecer(arranjo)


def test_validar_arranjo_charlie_7() -> None:
    arranjo = "HMmhhhhhhhhhhhhhhhhhhmhhhhhhhhhhhhhh"
    assert verif_charlie.reconhecer(arranjo)


#### TESTES DELTA ####
# Casais heterossexuais mais velhos que os filhos, com pelo menos seis
# filhos, em que os dois primeiros filhos formam um casal e os ultimos
# também.

def test_validar_arranjo_delta_1() -> None:
    arranjo = "HMmhhmmh"
    assert verif_delta.reconhecer(arranjo) == 0


def test_validar_arranjo_delta_2() -> None:
    arranjo = "HHmhmh"
    assert verif_delta.reconhecer(arranjo) == 0


def test_validar_arranjo_delta_3() -> None:
    arranjo = "MMmhmhmm"
    assert verif_delta.reconhecer(arranjo) == 0


def test_validar_arranjo_delta_4() -> None:
    arranjo = "HHhhmmmh"
    assert verif_delta.reconhecer(arranjo) == 0


def test_validar_arranjo_delta_5() -> None:
    arranjo = "HHhmhhhhhhhhhmhmhmhmmhmhmhmm"
    assert verif_delta.reconhecer(arranjo) == 0


def test_validar_arranjo_delta_6() -> None:
    arranjo = "MMhmhhm"
    assert verif_delta.reconhecer(arranjo) == 0


def test_validar_arranjo_delta_7() -> None:
    arranjo = "HHmhhhhhhhhhhhhhhhhhhmhhhhhhhhhhhhhm"
    assert verif_delta.reconhecer(arranjo)


def test_validar_arranjo_delta_8() -> None:
    arranjo = "MMmhmmmmmmmmmmmmhmhmh"
    assert verif_delta.reconhecer(arranjo)


def test_validar_arranjo_delta_9() -> None:
    arranjo = "MMhmmhmh"
    assert verif_delta.reconhecer(arranjo)


#### TESTES ECHO ####
# Casais homossexuais mais velhos que os filhos, em que o sexo dos
# filhos é alternado conforme a ordem de nascimento.

def test_validar_arranjo_echo_1() -> None:
    arranjo = "HMm"
    assert verif_echo.reconhecer(arranjo) == 0


def test_validar_arranjo_echo_2() -> None:
    arranjo = "MHmhm"
    assert verif_echo.reconhecer(arranjo) == 0


def test_validar_arranjo_echo_3() -> None:
    arranjo = "HHmhhmh"
    assert verif_echo.reconhecer(arranjo) == 0


def test_validar_arranjo_echo_4() -> None:
    arranjo = "MMm"
    assert verif_echo.reconhecer(arranjo) == 0


def test_validar_arranjo_echo_5() -> None:
    arranjo = "HHhmhmhmhm"
    assert verif_echo.reconhecer(arranjo)


def test_validar_arranjo_echo_6() -> None:
    arranjo = "MMhmhmhmhm"
    assert verif_echo.reconhecer(arranjo)


def test_validar_arranjo_echo_7() -> None:
    arranjo = "HHmhmhm"
    assert verif_echo.reconhecer(arranjo)


def test_validar_arranjo_echo_8() -> None:
    arranjo = "HHh"
    assert verif_echo.reconhecer(arranjo)


def test_validar_arranjo_echo_9() -> None:
    arranjo = "MMh"
    assert verif_echo.reconhecer(arranjo)


def test_validar_arranjo_echo_10() -> None:
    arranjo = "HHmhm"
    assert verif_echo.reconhecer(arranjo)


#### TESTES FOXTROT ####
# Casais homossexuais mais velhos que os filhos, com qualquer quantidade
# de filhos homens e mulheres, mas que nâo tiveram dois filhos homens
# consecutivos

def test_validar_arranjo_foxtrot_1() -> None:
    arranjo = "HMm"
    assert verif_foxtrot.reconhecer(arranjo) == 0


def test_validar_arranjo_foxtrot_2() -> None:
    arranjo = "HHhh"
    assert verif_foxtrot.reconhecer(arranjo) == 0


def test_validar_arranjo_foxtrot_3() -> None:
    arranjo = "MMmhhm"
    assert verif_foxtrot.reconhecer(arranjo) == 0


def test_validar_arranjo_foxtrot_4() -> None:
    arranjo = "HH"
    assert verif_foxtrot.reconhecer(arranjo)


def test_validar_arranjo_foxtrot_5() -> None:
    arranjo = "MM"
    assert verif_foxtrot.reconhecer(arranjo)


def test_validar_arranjo_foxtrot_6() -> None:
    arranjo = "HHhmmhmhmmh"
    assert verif_foxtrot.reconhecer(arranjo)


def test_validar_arranjo_foxtrot_7() -> None:
    arranjo = "HHhmh"
    assert verif_foxtrot.reconhecer(arranjo)


#### TESTES GOLF ####
# Arranjo de no minimo x∈N e no maximo y∈N, com x>0, y>0, e x<=y, de
# adultos (Hs ou Ms) mais velhos que os filhos, com qualquer quantidade
# de filhos homens e mulheres, mas que os três filhos mais novos não
# foram homens.

def test_validar_arranjo_golf_1() -> None:
    arranjo = "HHHMMhmhmhmhm"
    assert verif_golf.reconhecer(arranjo) == 0


def test_validar_arranjo_golf_2() -> None:
    arranjo = "HHHMMMhhh"
    assert verif_golf.reconhecer(arranjo) == 0


def test_validar_arranjo_golf_3() -> None:
    arranjo = "MMHHHmhmmmmhmhhhh"
    assert verif_golf.reconhecer(arranjo) == 0


def test_validar_arranjo_golf_4() -> None:
    arranjo = "HHHMMMhh"
    assert verif_golf.reconhecer(arranjo)


def test_validar_arranjo_golf_5() -> None:
    arranjo = "HHHMMMMhhhm"
    assert verif_golf.reconhecer(arranjo)


def test_validar_arranjo_golf_6() -> None:
    arranjo = "HMmhmhmhmmhh"
    assert verif_golf.reconhecer(arranjo)
