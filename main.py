from src.checa_campos_form import checa_campos_form


print("""\
    Escolha a funcionalidade desejada:
    1: Máscara de validação de campos de um formulário
    2: Gerar arranjos familiares
""")
funcionalidade = int(input("Sua escolha: "))

if funcionalidade == 1:
    nome = checa_campos_form.validar_nome
    nome.__name__ = "validar_nome"
    email = checa_campos_form.validar_email
    email.__name__ = "validar_email"
    senha = checa_campos_form.validar_senha
    senha.__name__ = "validar_senha"
    cpf = checa_campos_form.validar_cpf
    cpf.__name__ = "validar_cpf"
    telefone = checa_campos_form.validar_telefone
    telefone.__name__ = "validar_telefone"
    datetime = checa_campos_form.validar_datetime
    datetime.__name__ = "validar_datetime"
    numero = checa_campos_form.validar_numero
    numero.__name__ = "validar_numero"
    
    opcoes = {
        "1": nome,
        "2": email,
        "3": senha,
        "4": cpf,
        "5": telefone,
        "6": datetime,
        "7": numero,
    }
    
    print("Escolha uma opção: ")
    for numero, opcao in opcoes.items():
        print(f"{numero} - {opcao.__name__}")
    escolha = opcoes[input("Número escolhido: ")]

    # verificador = Verificador(escolha)
    # entrada = input("Qual o valor a ser verificado? ")
    # resultado = verificador.reconhecer(entrada)

    # print(f"{str(escolha)} é {'valido(a)' if resultado else 'invalido(a)'}")

    
