import re


def caso_alfa(str: arranjo) -> bool:
    """Reconhece casais heterossexuais mais velhos que os filhos com
    pelo menos duas filhas mulheres, ou pelo menos um filho homem, ou
    ainda pelo menos dois filhos homens e uma filha mulher.

    Args:
        arranjo {str} -- um arranjo familiar

    Retorna:
        {bool}
    """

    regra = r'HM|MH(?=(.*h.*|.*m.*m.*|.*m.*)[hm]{3}'
    reconhecido = re.search(regra)
    return bool(reconhecido)


def caso_beta(str: arranjo) -> bool:
    pass


def caso_charlie(str: arranjo) -> bool:
    pass


def caso_delta(str: arranjo) -> bool:
    pass


def caso_echo(str: arranjo) -> bool:
    pass


def caso_foxtrot(str: arranjo) -> bool:
    pass


def caso_golf(str: arranjo) -> bool:
    pass



