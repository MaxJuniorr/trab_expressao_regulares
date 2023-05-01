from typing import Callable
import random


def criar_casais_hetero() -> str:
    return ''.join(random.choices(('HM', 'MH'), k=1))


def criar_casais_homo() -> str:
    return ''.join(random.choices(('HH', 'MM'), k=1))


def criar_nsais_platonico(x:int, y: int) -> str:
    assert x <= y and x > 0 and y > 0, "Os parâmetros não obedecem a regra x > 0, y > 0 , e x <= y"

    def nsal_concreto():

        n_sorteado = random.randint(x, y) if x != y else x
        return ''.join(random.choices('HM', k=n_sorteado))
    return nsal_concreto

########## filhos
# [WARNING] Regras que definem tamanho devem ser aplicadas primeiro

def _iniciar_prole() -> str:
    '''Cria uma prole combinando "h" e "m" de tamanho n'''
    n = random.randint(0,100)
    return ''.join(random.choices('hm', k=n))


def floor6_prole(cadeia: str) -> str:
    """Retorna uma prole de tamanho mínimo 6."""
    tam = len(cadeia)
    if tam >= 6:
        return cadeia, True
    return cadeia + ''.join(random.choices('hm', k=6-tam)), False

# funções limite
def floor_h(cadeia: str, n: int, modificar: bool = None, na: int = None) -> str:
    """Retorna uma string com pelo menos n 'h's."""

    #Resolvendo um limite que já veio anteriormente
    if not(modificar == None and na == None) and len(cadeia) < n+na:
        cadeia = "m"*(n+na)
        i = 0
        while i < n:
            indice = random.randint(0, len(cadeia) - 1)
            if cadeia[indice] != "h":
                cadeia = cadeia[:indice] + "h" + cadeia[indice + 1:]
                i += 1
        return cadeia

    # resolver problema com len(cadeia) < n ocorre loop infinito
    if len(cadeia) <= n:
        return ''.join(random.choices('h', k=n))
    
    
    qtd = cadeia.count('h')
    controle = n - qtd

    if controle <= 0:
        return cadeia

    i = 0
    while i < controle:
        indice = random.randint(0, len(cadeia) - 1)
        if cadeia[indice] != "h":
            cadeia = cadeia[:indice] + "h" + cadeia[indice + 1:]
            i += 1
    return cadeia


def floor_m(cadeia: str, n: int, modificar: bool = None, na: int = None) -> str:
    """Retorna uma string com pelo menos n 'm's."""

    #Resolvendo um limite que já veio anteriormente
    if not(modificar == None and na == None) and len(cadeia) < n+na:
        cadeia = "h"*(n+na)
        i = 0
        while i < n:
            indice = random.randint(0, len(cadeia) - 1)
            if cadeia[indice] != "m":
                cadeia = cadeia[:indice] + "m" + cadeia[indice + 1:]
                i += 1
        return cadeia


    # resolver problema com len(cadeia) < n ocorre loop infinito
    if len(cadeia) <= n:
        return ''.join(random.choices('m', k=n))
    
    qtd = cadeia.count('m')
    controle = n - qtd

    if controle <= 0:
        return cadeia

    i = 0
    while i < controle:
        indice = random.randint(0, len(cadeia) - 1)
        if cadeia[indice] != "m":
            cadeia = cadeia[:indice] + "m" + cadeia[indice + 1:]
            i += 1
    return cadeia

#A priori, estou deduzindo que as cadeias de ceil não precisam de modificação
def ceil_h(cadeia: str, n: int) -> str:
    """Retorna uma string com no máximo n 'h's."""

    qtd = cadeia.count('h')
    if qtd <= n:
        return cadeia, True

    controle = qtd - n
    i = 0
    while i < controle:
        indice = random.randint(0, len(cadeia) - 1)
        if cadeia[indice] != "m":
            cadeia = cadeia[:indice] + "m" + cadeia[indice + 1:]
            i += 1
    return cadeia, False

#A priori, estou deduzindo que as cadeias de ceil não precisam de modificação
def ceil_m(cadeia: str, n: int) -> str:
    """Retorna uma string com no máximo n 'm's."""
    
    qtd = cadeia.count('m')
    if qtd <= n:
        return cadeia, True

    controle = qtd - n
    i = 0
    while i < controle:
        indice = random.randint(0, len(cadeia) - 1)
        if cadeia[indice] != "h":
            cadeia = cadeia[:indice] + "h" + cadeia[indice + 1:]
            i += 1
    return cadeia, False

def impar_h(cadeia: str) -> str:
    """Retorna uma string com uma quantidade impar de 'h's."""
    # cadeia vazia não faz parte da linguagem, retorna o caso mínimo
    if len(cadeia) == 0:
        return "".join("h"), False
    
    num_m = cadeia.count('h')

    # se a regra ja estiver satisfeita, não muda a cadeia e retorna True pro validador
    if num_m % 2 != 0:
        return cadeia, True 
    
    # se só tiver "h" e a regra não for satisfeita, trocamos um "h" por "m"
    if cadeia.count('m') == 0:
        indice = random.randint(0, len(cadeia)-1)
        return cadeia[:indice] + 'm' + cadeia[indice+1:], False
    
    # se tiver "h" e "m" um "m" é sorteado para tornar-se "h"
    indice = random.randint(0, len(cadeia)-1)
    while cadeia[indice] == 'h':
        indice = random.randint(0, len(cadeia)-1)
    cadeia = cadeia[:indice] + 'h' + cadeia[indice+1:]
    return cadeia, False
    

def impar_m(cadeia: str) -> str:
    """Retorna uma string com uma quantidade impar de 'm's."""
    # cadeia vazia não faz parte da linguagem, retorna o caso mínimo
    if len(cadeia) == 0:
        return "".join("m"), False

    num_m = cadeia.count('m')

    # se a regra ja estiver satisfeita, não muda a cadeia e retorna True pro validador
    if num_m % 2 != 0:
        return cadeia, True 

    # se só tiver "m" e a regra não for satisfeita, trocamos um "m" por "h"
    if cadeia.count('h') == 0:
        indice = random.randint(0, len(cadeia)-1)
        return cadeia[:indice] + 'h' + cadeia[indice+1:], False
    
    # se tiver "h" e "m" um "m" é sorteado para tornar-se "h"
    indice = random.randint(0, len(cadeia)-1)
    while cadeia[indice] == 'm':
        indice = random.randint(0, len(cadeia)-1)
    cadeia = cadeia[:indice] + 'm' + cadeia[indice+1:]
    return cadeia, False


def par_h(cadeia: str) -> str:
    """Retorna uma string com uma quantidade par de 'h's."""
    num_h = cadeia.count('h')
    if num_h % 2 != 0:
        return cadeia, True
    indice = random.randint(len(cadeia))
    cadeia = cadeia[:indice] + 'h' + cadeia[indice+1:]
    return cadeia, False


def par_m(cadeia: str) -> str:
    """Retorna uma string com uma quantidade par de 'm's."""
    num_m = cadeia.count('h')
    if num_m % 2 != 0:
        return cadeia, True
    indice = random.randint(len(cadeia))
    cadeia = cadeia[:indice] + 'm' + cadeia[indice+1:]
    return cadeia, False


def mais_novo_h(cadeia: str) -> str:
    """Retorna uma string em que o filho mais velho é h"""

    # cadeia vazia não faz parte da linguagem, retorna o caso mínimo
    if len(cadeia) == 0:
        return "".join('h'), False
    # para um caso de regra conjunta
    if len(cadeia) == 1 and cadeia[0] == 'm':
        return cadeia + 'h', False

    if cadeia[-1] == 'h':
        return cadeia, True
    cadeia = cadeia[:-1] + 'h'
    return cadeia, False


def mais_novo_m(cadeia: str) -> str:
    """Retorna uma string em que o filho mais velho é m"""

    # cadeia vazia não faz parte da linguagem, retorna o caso mínimo
    if len(cadeia) == 0:
        return "".join('m'), False
    # para um caso de regra conjunta
    if len(cadeia) == 1 and cadeia[0] == 'h':
        return cadeia + 'm', False
    
    if cadeia[-1] == 'm':
        return cadeia, True
    cadeia = cadeia[:-1] + 'm'
    return cadeia, False


def mais_velho_h(cadeia: str) -> str:
    """Retorna uma string em que o filho mais novo é h"""

    # cadeia vazia não faz parte da linguagem, retorna o caso mínimo
    if len(cadeia) == 0:
        return "".join('h'), False
    # para um caso de regra conjunta
    if len(cadeia) == 1 and cadeia[0] == 'm':
        return 'h' + cadeia, False

    if cadeia[0] == 'h':
        return cadeia, True
    cadeia = 'h' + cadeia[1:]
    return cadeia, False


def mais_velho_m(cadeia: str) -> str:
    """Retorna uma string em que o filho mais novo é m"""

    # cadeia vazia não faz parte da linguagem, retorna o caso mínimo
    if len(cadeia) == 0:
        return "".join('m'), False
    # para um caso de regra conjunta
    if len(cadeia) == 1 and cadeia[0] == 'h':
        return 'm' + cadeia, False

    if cadeia[0] == 'm':
        return cadeia, True
    cadeia = 'm' + cadeia[1:]
    return cadeia, False


def casal_primeiro(cadeia: str) -> str:
    """Retorna uma string em que os dois primeiros elementos formam um
    casal.
    """
    if (cadeia[0:2] == 'hm') or (cadeia[0:2] == 'mh'):
        return cadeia, True
    casal_random = random.choice(('hm', 'mh'))
    cadeia = casal_random + cadeia[2:]
    return cadeia, False


def casal_ultimo(cadeia: str) -> str:
    """Retorna uma string em que os dois últimos elementos formam um
    casal.
    """
    if (cadeia[-2:] == 'hm') or (cadeia[-2:] == 'mh'):
        return cadeia, True
    casal_random = random.choice(('hm', 'mh'))
    cadeia = cadeia[:-2] + casal_random
    return cadeia, False


# [WARNING] Prioridade
def filhos_alternados(cadeia: str) -> str:
    """Retorna uma string em que os filhos são alternados entre h e m."""
    nova_cadeia = []
    casal = random.choice(('hm', 'mh'))
    alvo = 0
    for _ in cadeia:
        nova_cadeia.append(casal[alvo])
        alvo = 1 if alvo == 0 else 0
      
    return "".join(nova_cadeia), True


# [NOTE] Testar isso
def nao_filhos_h_consecutivos(cadeia: str) -> str:
    """Retorna uma string em que não há filhos h consecutivos."""
    if 'hh' not in cadeia:
        return cadeia, True
    while 'hh' in cadeia:
        indice = cadeia.index('hh')
        casal_random = random.choice(('hm', 'mh', 'mm'))
        cadeia = cadeia[:indice] + casal_random + cadeia[indice+2:]
    return cadeia, False


def nao_filhos_m_consecutivos(cadeia: str) -> str:
    """Retorna uma string em que não há filhos m consecutivos."""
    if 'mm' not in cadeia:
        return cadeia, True
    while 'mm' in cadeia:
        indice = cadeia.index('mm')
        casal_random = random.choice(('hm', 'mh', 'hh'))
        cadeia = cadeia[:indice] + casal_random + cadeia[indice+2:]
    return cadeia, False


def nao_ultimos3_h_consecutivos(cadeia: str) -> str:
    """Retorna uma string em que não há 3 'h's consecutivos no final."""
    if 'hhh' != cadeia[-3:]:
        return cadeia, True
    random_element = random.randint(-3, -1)
    if random_element == -1:
        cadeia = cadeia[:-1] + 'm'
        return cadeia
    cadeia = cadeia[:random_element] + 'm' + cadeia[random_element+1:]
    return cadeia, False


def disjuncao(*opcoes) -> str:
    def interior() -> str:
        regras = [opcao() for opcao in opcoes]
        chosen = random.choice(regras)
        return chosen
    return interior
    

def gerador_arranjo(*regras_prole: Callable[[str], str], regra_pais=criar_casais_hetero, regra_limites: tuple =None, int_params: tuple =None) -> Callable[[], str]:
    """Retorna uma função que gera strings que satisfazem todas as
    regras passadas.
    """

    def gerar_arranjo() -> str:
        """Retorna uma string aleatória."""
        base = _iniciar_prole()
        
        if regra_limites and int_params:
            for i in range(len(regra_limites)):
                if i == 1:
                    base = regra_limites[i](base, int_params[i], True, int_params[i-1])
                else:
                    base = regra_limites[i](base, int_params[i])

        validador = 0
        while validador != 1:
            validador = 1
            for regra in regras_prole:
                base = regra(base)[0]
                validador *= regra(base)[1]
        return regra_pais() + base
    
    return gerar_arranjo
