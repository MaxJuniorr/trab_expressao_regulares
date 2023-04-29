import itertools
import random


def criar_casais_hetero() -> str:
    return ''.join(random.choices(('HM', 'MH'), k=1))


def criar_casais_homo() -> str:
    return ''.join(random.choices(('HH', 'MM'), k=1))


def criar_nsais_platonico(n:int) -> str:
    return ''.join(random.choices('HM', k=n))


def floor6_prole(n: int) -> str:
    """Retorna uma prole de tamanho mínimo 6."""
    pass


def floor_h(n: int) -> str:
    """Retorna uma string com pelo menos n 'h's."""
    pass


def floor_m(n: int) -> str:
    """Retorna uma string com pelo menos n 'm's."""
    pass


def ceil_h(n:int) -> str:
    """Retorna uma string com no máximo n 'h's."""
    pass


def ceil_m(n: int) -> str:
    """Retorna uma string com no máximo n 'm's."""
    pass

def impar_h() -> str:
    """Retorna uma string com uma quantidade impar de 'h's."""
    pass


def impar_m() -> str:
    """Retorna uma string com uma quantidade impar de 'm's."""
    pass


def par_h() -> str:
    """Retorna uma string com uma quantidade par de 'h's."""
    pass


def par_m() -> str:
    """Retorna uma string com uma quantidade par de 'm's."""
    pass


def mais_velho_h() -> str:
    """Retorna uma string em que o filho mais velho é h"""
    pass


def mais_velho_m() -> str:
    """Retorna uma string em que o filho mais velho é m"""
    pass


def mais_novo_h() -> str:
    """Retorna uma string em que o filho mais novo é h"""
    pass


def mais_novo_m() -> str:
    """Retorna uma string em que o filho mais novo é m"""
    pass


def casal_primeiro() -> str:
    """Retorna uma string em que os dois primeiros elementos formam um
    casal.
    """
    pass


def casal_ultimo() -> str:
    """Retorna uma string em que os dois últimos elementos formam um
    casal.
    """
    pass


def filhos_alternados() -> str:
    """Retorna uma string em que os filhos são alternados entre h e m."""
    pass


def nao_filhos_h_consecutivos() -> str:
    """Retorna uma string em que não há filhos h consecutivos."""
    pass


def nao_filhos_m_consecutivos() -> str:
    """Retorna uma string em que não há filhos m consecutivos."""
    pass


def nao_ultimos3_h_consecutivos() -> str:
    """Retorna uma string em que não há 3 'h's consecutivos no final."""
    pass


def criar_prole(n: int) -> str:
    '''Cria uma prole combinando "h" e "m" de tamanho n'''
    return ''.join(random.choices('hm', k=n))