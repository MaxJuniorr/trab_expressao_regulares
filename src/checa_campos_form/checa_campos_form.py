from src.common.gera_verificador import verificador


@verificador
def validar_nome() -> str:
    """
    Verifica se o nome analisado está dentro das regras de produção.

    Regras
    - Devem ser fornecidos no mínimo um nome e um sobrenome
    - Os nomes devem ser separados por um único espaço
    - O nome do meio é opcional
    - Não são permitidos caracteres especiais ou números
    - A primeira letra de cada nome deve ser maiúscula
    """

    return r"([A-Z][a-z]*)\s([A-Z][a-z]*\s)?[A-Z][a-z]*"


@verificador
def validar_email() -> str:
    """
    Verifica se o endereço de email analisado está dentro das
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

    return r"[a-z]+@[a-z]+(\.com)?\.br"


@verificador
def validar_senha() -> str:
    """
    Verifica se a senha analisada obedece às regras de produção.
    
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
    return r"^(?=.*[A-Z])(?=.*\d)\w{8}$"


@verificador
def validar_cpf() -> str:
    """
    Verifica se o número de cpf analisado está dentro das regras de
    produção.
    
    Regras
    - O cpf deve conter apenas números
    - O cpf é constituído de três cadeias de três números separados por
        um '.' seguidas por um '-' e uma cadeia de dois números. 
        
      Ex: 'nnn.nnn.nnn-nn', onde n é um numeral
    """

    return r"(\d{3}\.){2}\d{3}\-\d{2}"


@verificador
def validar_telefone() -> str:
    """
    Verifica se o número de telefone está dentro das regras de
    produção.

    Regras
    - Números de telefone devem ter um dos seguintes formatos:
        - (xx) 9xxxx-xxxx
        - (xx) 9xxxxxxxxxx
        - xx 9xxxxxxxx
    onde x é um numeral
    """

    # Explicação do regex do grupo inicial:
    # ^((\d{2}(?!.*\-.*)) -- ou começa com 2 digitos, se acontecer isso
    #                        vai procurar um hifen adiante, e só vai
    #                        reconhecer cadeias que não tenham o hífen.
    # |(\(\d{2}\)))       -- ou começa com dois digitos entre parenteses
    # ---------------------
    # Regex após o grupo inicial
    # \s9\d{4}-?\d{4}$    -- tem um espaço após o grupo inicial, seguido
    #                        de quadro digitos, seguido de um hífen
    #                        opcional, seguido de mais quatro dígitos, e
    #                        deve encerrar a cadeia neste ponto.
    return r"^((\d{2}(?!.*\-.*))|(\(\d{2}\)))\s9\d{4}-?\d{4}$"


@verificador
def validar_datetime() -> str:
    """
    Verifica se o datetime está dentro das regras de
    produção.

    Regras
    - Sentenças devem ter o formato dd/mm/aaaa hh:mm:ss,
    onde d, m, a, h, m, s são numerais
    """

    return r"^(\d\d/){2}\d{4} (\d\d:){2}\d{2}$"


@verificador
def validar_numero() -> str:
    """
    Verifica se o número está dentro das regras de
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
    
    return r"^[+-]?\d+(\.\d+)?$"
