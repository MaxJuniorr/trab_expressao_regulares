import re


def validar_caso_alfa(arranjo: str) -> bool:
    """Reconhece casais heterossexuais mais velhos que os filhos com
    pelo menos duas filhas mulheres, ou pelo menos um filho homem, ou
    ainda pelo menos dois filhos homens e uma filha mulher.

    Args:
        arranjo {str} -- um arranjo familiar

    Retorna:
        {bool}
    """

    subregra1 = r'(HM)|(MH)'
    subregra2 = r'[hm]*m[hm]*m[hm]*'
    subregra3 = r'[hm]*h[hm]*'
    subregra4 = r'([hm]*h[hm]*h[m]*|[hm]*h[m]*h[hm]*|[m]*h[hm]*h[hm]*)'
    regra = fr"^({subregra1})({subregra2}|{subregra3}|{subregra4})$"
    print(regra)
    reconhecido = re.search(regra, arranjo)
    return bool(reconhecido)

validar_caso_alfa("HMmhh")
def validar_caso_beta(arranjo: str) -> bool:
    pass


def validar_caso_charlie(arranjo: str) -> bool:
    pass


def validar_caso_delta(arranjo: str) -> bool:
    pass


def validar_caso_echo(arranjo: str) -> bool:
    pass


def validar_caso_foxtrot(arranjo: str) -> bool:
    pass


def validar_caso_golf(arranjo: str) -> bool:
    pass



