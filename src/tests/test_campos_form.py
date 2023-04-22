from src.checa_campos_form import checa_campos_form
from src.common import helper
import pytest

# Instanciando os reconhecedores para cada tipo de dado
nome = checa_campos_form.Nome()
verif_nome = checa_campos_form.Verificador(nome)

email = checa_campos_form.Email()
verif_email = checa_campos_form.Verificador(email)

senha = checa_campos_form.Senha()
verif_senha = checa_campos_form.Verificador(senha)

cpf = checa_campos_form.Cpf()
verif_cpf = checa_campos_form.Verificador(cpf)

telefone = checa_campos_form.Telefone()
verif_telefone = checa_campos_form.Verificador(telefone)

datetime = checa_campos_form.Datetime()
verif_datetime = checa_campos_form.Verificador(datetime)

numero = checa_campos_form.Numero()
verif_numero = checa_campos_form.Verificador(numero)


#### TESTES NOME ####
def test_validar_nome_1() -> None:
    nome = "Ada Lovelace"
    assert verif_nome.reconhecer(nome)


def test_validar_nome_2() -> None:
    nome = "Stephen Cole Kleene"
    assert verif_nome.reconhecer(nome)


def test_validar_nome_3() -> None:
    nome = "1Alan"
    assert verif_nome.reconhecer(nome) == 0, "O primeiro caracter do nome precisa ser uma letra"


def test_validar_nome_4() -> None:
    nome = "alan"
    assert verif_nome.reconhecer(nome) == 0, "Nomes devem iniciar com letra maiúscula"


def test_validar_nome_5() -> None:
    nome = "A1an"
    assert verif_nome.reconhecer(nome) == 0, "Nomes não aceitam caracteres especiais ou números"


def test_validar_nome_6() -> None:
    nome = "A1an Turing"
    assert verif_nome.reconhecer(nome) == 0, "Nomes não aceitam caracteres especiais ou números"


#### TESTES EMAIL ####
def test_validar_email_1() -> None:
    email = "a@a.br"
    assert verif_email.reconhecer(email)


def test_validar_email_2() -> None:
    email = "a@a.com.br"
    assert verif_email.reconhecer(email)


def test_validar_email_3() -> None:
    email = "divulga@ufpa.br"
    assert verif_email.reconhecer(email)


def test_validar_email_4() -> None:
    email = "@"
    assert verif_email.reconhecer(email) == 0


def test_validar_email_5() -> None:
    email = "a@.br"
    assert verif_email.reconhecer(email) == 0


def test_validar_email_6() -> None:
    email = "@a.br"
    assert verif_email.reconhecer(email) == 0


def test_validar_email_7() -> None:
    email = "T@teste.br"
    assert verif_email.reconhecer(email) == 0


def test_validar_email_8() -> None:
    email = "a@A.com.br"
    assert verif_email.reconhecer(email) == 0


#### TESTES SENHA ####
def test_validar_senha_1() -> None:
    senha = "518R2r5e"
    assert verif_senha.reconhecer(senha)


def test_validar_senha_2() -> None:
    senha = "F123456A"
    assert verif_senha.reconhecer(senha)


def test_validar_senha_3() -> None:
    senha = "1234567T"
    assert verif_senha.reconhecer(senha)


def test_validar_senha_4() -> None:
    senha = "ropsSoq0"
    assert verif_senha.reconhecer(senha)


def test_validar_senha_5() -> None:
    senha = "F1234567A"
    assert verif_senha.reconhecer(senha) == 0


def test_validar_senha_6() -> None:
    senha = "abcdefgH"
    assert verif_senha.reconhecer(senha) == 0


def test_validar_senha_7() -> None:
    senha = "1234567HI"
    assert verif_senha.reconhecer(senha) == 0


#### TESTES CPF ####
def test_validar_cpf_1() -> None:
    cpf = "123.456.789-09"
    assert verif_cpf.reconhecer(cpf)


def test_validar_cpf_2() -> None:
    cpf = "000.000.000-00"
    assert verif_cpf.reconhecer(cpf)


def test_validar_cpf_3() -> None:
    cpf = "123.456.789-0"
    assert verif_cpf.reconhecer(cpf) == 0


def test_validar_cpf_4() -> None:
    cpf = "111.111.11-11"
    assert verif_cpf.reconhecer(cpf) == 0


#### TESTES TELEFONE ####
def test_validar_telefone_1() -> None:
    telefone = "(91) 99999-9999"
    assert verif_telefone.reconhecer(telefone)


def test_validar_telefone_2() -> None:
    telefone = "(91) 999999999"
    assert verif_telefone.reconhecer(telefone)


def test_validar_telefone_3() -> None:
    telefone = "91 999999999"
    assert verif_telefone.reconhecer(telefone)


def test_validar_telefone_4() -> None:
    telefone = "(91) 59999-9999"
    assert verif_telefone.reconhecer(telefone) == 0


def test_validar_telefone_5() -> None:
    telefone = "99 99999-9999"
    assert verif_telefone.reconhecer(telefone) == 0


def test_validar_telefone_6() -> None:
    telefone = "(94)95555-5555"
    assert verif_telefone.reconhecer(telefone) == 0


#### TESTES DATETIME ####
def test_validar_datetime_1() -> None:
    datetime = "31/08/2019 20:14:55"
    assert verif_datetime.reconhecer(datetime)


def test_validar_datetime_2() -> None:
    datetime = "99/99/9999 23:59:59"
    assert verif_datetime.reconhecer(datetime)


def test_validar_datetime_3() -> None:
    datetime = "99/99/9999 3:9:9"
    assert verif_datetime.reconhecer(datetime) == 0


def test_validar_datetime_4() -> None:
    datetime = "9/9/99 99:99:99"
    assert verif_datetime.reconhecer(datetime) == 0


def test_validar_datetime_5() -> None:
    datetime = "99/99/999903:09:09"
    assert verif_datetime.reconhecer(datetime) == 0


#### TESTES NUMERO ####
def test_validar_numero_1() -> None:
    numero = "-25.467"
    assert verif_numero.reconhecer(numero)


def test_validar_numero_2() -> None:
    numero = "1"
    assert verif_numero.reconhecer(numero)


def test_validar_numero_3() -> None:
    numero = "-1"
    assert verif_numero.reconhecer(numero)


def test_validar_numero_4() -> None:
    numero = "+1"
    assert verif_numero.reconhecer(numero)


def test_validar_numero_5() -> None:
    numero = "64.2"
    assert verif_numero.reconhecer(numero)


def test_validar_numero_6() -> None:
    numero = "1."
    assert verif_numero.reconhecer(numero) == 0


def test_validar_numero_7() -> None:
    numero = ".2"
    assert verif_numero.reconhecer(numero) == 0


def test_validar_numero_8() -> None:
    numero = "+64,2"
    assert verif_numero.reconhecer(numero) == 0
