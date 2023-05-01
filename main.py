from src.checa_campos_form import checa_campos_form


print("""\
    Escolha a funcionalidade desejada:
    1: Máscara de validação de campos de um formulário
    2: Gerar arranjos familiares
""")
funcionalidade = int(input("Sua escolha: "))

if funcionalidade == 1:
    nome = checa_campos_form.validar_nome
    email = checa_campos_form.validar_email
    senha = checa_campos_form.validar_senha
    cpf = checa_campos_form.validar_cpf
    telefone = checa_campos_form.validar_telefone
    datetime = checa_campos_form.validar_datetime
    numero = checa_campos_form.validar_numero
    
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
    entrada = input("Valor a ser verificado: ")
    resultado = escolha(entrada)

    print(f"{entrada} é {'valido(a)' if resultado else 'invalido(a)'}")

    
