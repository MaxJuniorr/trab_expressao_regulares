from src.checa_campos_form import checa_campos_form
from src.common import helper


#### TESTES NOME ####
def test_validar_nome_1() -> None:
    nome = "Ada Lovelace"
    assert checa_campos_form.validar_nome(nome)


def test_validar_nome_2() -> None:
    nome = "Stephen Cole Kleene"
    assert checa_campos_form.validar_nome(nome)


def test_validar_nome_3() -> None:
    nome = "1Alan"
    assert checa_campos_form.validar_nome(nome) == 0, "O primeiro caracter do nome precisa ser uma letra"


def test_validar_nome_4() -> None:
    nome = "alan"
    assert checa_campos_form.validar_nome(nome) == 0, "Nomes devem iniciar com letra maiúscula"


def test_validar_nome_5() -> None:
    nome = "A1an"
    assert checa_campos_form.validar_nome(nome) == 0, "Nomes não aceitam caracteres especiais ou números"


def test_validar_nome_6() -> None:
    nome = "A1an Turing"
    assert checa_campos_form.validar_nome(nome) == 0, "Nomes não aceitam caracteres especiais ou números"


#### TESTES EMAIL ####
def test_validar_email_1() -> None:
    email = "a@a.br"
    assert checa_campos_form.validar_email(email)


def test_validar_email_2() -> None:
    email = "a@a.com.br"
    assert checa_campos_form.validar_email(email)


def test_validar_email_3() -> None:
    email = "divulga@ufpa.br"
    assert checa_campos_form.validar_email(email)


def test_validar_email_4() -> None:
    email = "@"
    assert checa_campos_form.validar_email(email) == 0


def test_validar_email_5() -> None:
    email = "a@.br"
    assert checa_campos_form.validar_email(email) == 0


def test_validar_email_6() -> None:
    email = "@a.br"
    assert checa_campos_form.validar_email(email) == 0


def test_validar_email_7() -> None:
    email = "T@teste.br"
    assert checa_campos_form.validar_email(email) == 0


def test_validar_email_8() -> None:
    email = "a@A.com.br"
    assert checa_campos_form.validar_email(email) == 0


#### TESTES SENHA ####
def test_validar_senha_1() -> None:
    senha = "518R2r5e"
    assert checa_campos_form.validar_senha(senha)


def test_validar_senha_2() -> None:
    senha = "F123456A"
    assert checa_campos_form.validar_senha(senha)


def test_validar_senha_3() -> None:
    senha = "1234567T"
    assert checa_campos_form.validar_senha(senha)


def test_validar_senha_4() -> None:
    senha = "ropsSoq0"
    assert checa_campos_form.validar_senha(senha)


def test_validar_senha_5() -> None:
    senha = "F1234567A"
    assert checa_campos_form.validar_senha(senha) == 0


def test_validar_senha_6() -> None:
    senha = "abcdefgH"
    assert checa_campos_form.validar_senha(senha) == 0


def test_validar_senha_7() -> None:
    senha = "1234567HI"
    assert checa_campos_form.validar_senha(senha) == 0


#### TESTES CPF ####
def test_validar_cpf_1() -> None:
    cpf = "123.456.789-09"
    assert checa_campos_form.validar_cpf(cpf)


def test_validar_cpf_2() -> None:
    cpf = "000.000.000-00"
    assert checa_campos_form.validar_cpf(cpf)


def test_validar_cpf_3() -> None:
    cpf = "123.456.789-0"
    assert checa_campos_form.validar_cpf(cpf) == 0


def test_validar_cpf_4() -> None:
    cpf = "111.111.11-11"
    assert checa_campos_form.validar_cpf(cpf) == 0


#### TESTES TELEFONE ####
def test_validar_telefone_1() -> None:
    telefone = "(91) 99999-9999"
    assert checa_campos_form.validar_telefone(telefone)


def test_validar_telefone_2() -> None:
    telefone = "(91) 999999999"
    assert checa_campos_form.validar_telefone(telefone)


def test_validar_telefone_3() -> None:
    telefone = "91 999999999"
    assert checa_campos_form.validar_telefone(telefone)


def test_validar_telefone_4() -> None:
    telefone = "(91) 59999-9999"
    assert checa_campos_form.validar_telefone(telefone) == 0


def test_validar_telefone_5() -> None:
    telefone = "99 99999-9999"
    assert checa_campos_form.validar_telefone(telefone) == 0


def test_validar_telefone_6() -> None:
    telefone = "(94)95555-5555"
    assert checa_campos_form.validar_telefone(telefone) == 0


#### TESTES DATETIME ####
def test_validar_datetime_1() -> None:
    datetime = "31/08/2019 20:14:55"
    assert checa_campos_form.validar_datetime(datetime)


def test_validar_datetime_2() -> None:
    datetime = "99/99/9999 23:59:59"
    assert checa_campos_form.validar_datetime(datetime)


def test_validar_datetime_3() -> None:
    datetime = "99/99/9999 3:9:9"
    assert checa_campos_form.validar_datetime(datetime) == 0


def test_validar_datetime_4() -> None:
    datetime = "9/9/99 99:99:99"
    assert checa_campos_form.validar_datetime(datetime) == 0


def test_validar_datetime_5() -> None:
    datetime = "99/99/999903:09:09"
    assert checa_campos_form.validar_datetime(datetime) == 0


#### TESTES NUMERO ####
def test_validar_numero_1() -> None:
    numero = "-25.467"
    assert checa_campos_form.validar_numero(numero)


def test_validar_numero_2() -> None:
    numero = "1"
    assert checa_campos_form.validar_numero(numero)


def test_validar_numero_3() -> None:
    numero = "-1"
    assert checa_campos_form.validar_numero(numero)


def test_validar_numero_4() -> None:
    numero = "+1"
    assert checa_campos_form.validar_numero(numero)


def test_validar_numero_5() -> None:
    numero = "64.2"
    assert checa_campos_form.validar_numero(numero)


def test_validar_numero_6() -> None:
    numero = "1."
    assert checa_campos_form.validar_numero(numero) == 0


def test_validar_numero_7() -> None:
    numero = ".2"
    assert checa_campos_form.validar_numero(numero) == 0


def test_validar_numero_8() -> None:
    numero = "+64,2"
    assert checa_campos_form.validar_numero(numero) == 0
