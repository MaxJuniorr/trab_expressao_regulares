import re


def validar_nome(nome: str) -> bool:
    """Verifica se o nome analisado está dentro das regras de produção.

    Regras
    - Devem ser fornecidos no mínimo um nome e um sobrenome
    - Os nomes devem ser separados por um único espaço
    - O nome do meio é opcional
    - Não são permitidos caracteres especiais ou números
    - A primeira letra de cada nome deve ser maiúscula
    """

    regra = r"([A-Z][a-z]*)\s([A-Z][a-z]*\s)?[A-Z][a-z]*"
    match = re.search(regra, nome)
    return bool(match)


def validar_email(email: str) -> bool:
    """Verifica se o endereço de email analisado está dentro das
regras de produção.

    Regras
    - Emails devem conter um, e apenas um, símbolo '@'
    - Todas as letras de um email devem ser minúsculas
    - Os endereços não podem conter símbolos especiais
        (excetuando-se o '@')
    - O símbolo '@' não pode ser usado no começo do endereço
    - Endereços devem terminar com '.com.br' ou '.br'
    - Endereços devem conter pelo menos uma letra minúscula 
        entre o símbolo '@' e a subcadeia '.com.br' ou a subcadeia '.br'
    """
    
    regra = r"[a-z]+@[a-z]+(\.com)?\.br"
    match = re.search(regra, email)
    return bool(match)


def validar_senha(senha: str) -> bool:
    """Verifica se a senha analisada está dentro das regras de produção.
    
    Regras
    - Senhas podem conter letras minúsculas, maiúsculas e/ou símbolos
    - Senhas devem conter pelo menos uma letra maiúsula e um número
    - Senhas devem ter o comprimento mínimo de 8 caracteres
    """
    
    # Explicação do regex:
    # (?=.*[A-Z])   -> positive lookaround para encontrar pelo menos
    #                   uma letra maiúscula
    # (?=.*\d)      -> positive lookaround para encontrar pelo menos
    #                   um número
    # [\w]{8}        -> aceita caracteres alfanuméricos, exatamente 8
    # ^...$          -> a cadeia precisa começar e terminar obedecendo
    #                   essas regras.
    #                   Isso evita o match parcial das 8 primeiras
    #                   ocorrências.
    regra = r"^(?=.*[A-Z])(?=.*\d)\w{8}$"
    match = re.search(regra, senha)
    return bool(match)


def validar_cpf(cpf: str) -> bool:
    """Verifica se o número de cpf analisado está dentro das regras de
produção.
    
    Regras
    - O cpf deve conter apenas números
    - O cpf é constituído de três cadeias de três números separados por
        um '.' seguidas por um '-' e uma cadeia de dois números. 
        
      Ex: 'nnn.nnn.nnn-nn', onde n é um numeral
    """
    
    regra = r"(\d{3}\.){2}\d{3}\-\d{2}"
    match = re.search(regra, cpf)
    return bool(match)


def validar_telefone(telefone: str) -> bool:
    """Verifica se o número de telefone está dentro das regras de
    produção.

    Regras
    - Números de telefone devem ter um dos seguintes formatos:
        - (xx) 9xxxx-xxxx
        - (xx) 9xxxxxxxxxx
<<<<<<< HEAD
        - 9xxxxxxxx
onde x é um numeral 
    """
    
    regra = r"^((\d{2}(?!.*\-.*))|(\(\d{2}\)))\s9\d{4}-?\d{4}$"
    match = re.search(regra, telefone)
    return bool(match)


def validar_datetime(datetime: str) -> bool:
    """Verifica se o número de telefone está dentro das regras de
    produção.

    Regras
    - Sentenças devem ter o formato dd/mm/aaaa hh:mm:ss,
    onde d, m, a, h, m, s são numerais
    """
    regra = r"^(\d\d/){2}\d{4} (\d\d:){2}\d{2}$"
    match = re.search(regra, datetime)
    return bool(match)


def validar_numero(numero: str) -> bool:
    """Verifica se o número de telefone está dentro das regras de
    produção.

    Regras
    - Números podem começar com um dos símbolos de {+, -}
    - Caso possuam um símbolo de sinal, o símbolo seguinte deve ser um
      numeral
    - Números devem possuir pelo menos um numeral
    - Números podem possuir um símbolo separador "." caso possuam uma
      parte fracionária
    - Caso possuam um separador, após o separador seguirá um numeral
    """
    regra = r"^[+-]?\d+(\.\d+)?$"
    match = re.search(regra, numero)
    return bool(match)