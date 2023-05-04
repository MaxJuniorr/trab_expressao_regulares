import re


def validar_arranjo_alfa(arranjo: str) -> bool:
    """Casais heterossexuais mais velhos que os filhos com
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
    reconhecido = re.search(regra, arranjo)
    return bool(reconhecido)


def validar_arranjo_beta(arranjo: str) -> bool:
    """Casais heterossexuais mais velhos que os filhos e com
    uma quantidade ímpar de filhas mulheres.
    
    Args:
        arranjo {str} -- um arranjo familiar
        
    Retorna:
        {boll}
    """

    regra = r"^(HM|MH)h*mh*((h*)m(h*)m(h*))*$"
    reconhecido = re.search(regra, arranjo)
    return bool(reconhecido)


def validar_arranjo_charlie(arranjo: str) -> bool:
    """Casais heterossexuais mais velhos que os filhos, com a 
    filha mais velha mulher e o filho mais novo homem.

    Args:
        arranjo {str} -- um arranjo familiar
    Retorna:
        {boll}
    """

    regra = r"^(HM|MH)m(m|h)*h$"
    reconhecido = re.search(regra, arranjo)
    return bool(reconhecido)



def validar_arranjo_delta(arranjo: str) -> bool:
    """Casais homossexuais mais velhos que os filhos, com
    pelo menos seis filhos, em que os dois primeiros filhos formam
    um casal e os últimos também.
    
    Args:
        arranjo {str} -- um arranjo familiar
        
    Retorna:
        {boll}"""
    
    regra = r"^(HH|MM)(hm|mh)(m|h){2}(m|h)*(hm|mh)$"
    reconhecido = re.search(regra, arranjo)
    return bool(reconhecido)

def validar_arranjo_echo(arranjo: str) -> bool:
    """Casais homossexuais mais velhos que os filhos, 
    em que o sexo dos filhos é alternado
    conforme a ordem de nascimento.
    
    Args:
        arranjo {str} -- um arranjo familiar

    Retorna:
        {bool}
    """
    
    regra = r"^(HH|MM)m?(hm)*h?$" #^(HH|MM)(h|m|(hm)+h?|(mh)+m?)$
    reconhecido = re.search(regra, arranjo)
    return bool(reconhecido)


def validar_arranjo_foxtrot(arranjo: str) -> bool:
    """Casais homossexuais mais velhos que os filhos, com
    qualquer quantidade de filhos homens e mulheres, mas
    que não tiveram dois filhos homens consecutivos.

    Args:
        arranjo {str} -- um arranjo familiar
    Retorna:
        {boll}
    """

    regra = r"^(HH|MM)h?m*(m+h)*m*$"
    reconhecido = re.search(regra, arranjo)
    return bool(reconhecido)


def validar_arranjo_golf(arranjo: str, x: int, y: int) -> bool:
    """Arranjo de no mínimo x ∈ N e no máximo y ∈ N, com x > 0, y > 0,
    e x ≤ y, de adultos (Hs ou Ms) mais velhos que os filhos, com
    qualquer quantidade de filhos homens e mulheres, mas que os três
    filhos mais novos não foram homens.

    Args:
        arranjo {str} -- um arranjo familiar
    Retorna:
        {bool}
    """

    # assert x <= y, "Os parâmetros não obedecem a regra x > 0, y > 0 , e x <= y"
    # Para escapar a chave da f-string, pode-se usar a sintaxe "{{" ao 
    # invés de "\{".
    assert x <= y and x > 0 and y > 0, "Os parâmetros não obedecem a regra x > 0, y > 0 , e x <= y"
    regra = fr"^(H|M){{{x},{y}}}(((h|m)*(m{{1,2}}|mh{{1,2}}))|h{{1,2}})?$" #!(hhh) ou  ^[hhh]
    reconhecido = re.search(regra, arranjo)
    return bool(reconhecido)
