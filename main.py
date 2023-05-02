from src.checa_campos_form import checa_campos_form
import src.arranjos_familiares.gerador_arranjos as ge
from src import demo
import random

# [TODO] - FORMATAR OUTPUT
print("""\
    Escolha a funcionalidade desejada:
    1: Máscara de validação de campos de um formulário
    2: Gerar arranjos familiares (Demonstração da 2ª questão)
    3: Gerar arranjos familiares (Implementação customizável)
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
    # [TODO] - FORMATAR OUTPUT
    print("Escolha uma opção: ")
    for numero, opcao in opcoes.items():
        print(f"{numero} - {opcao.__name__}")
    escolha = opcoes[input("Número escolhido: ")]
    entrada = input("Valor a ser verificado: ")
    resultado = escolha(entrada)
    print(f"{entrada} é {'valido(a)' if resultado else 'invalido(a)'}")

elif funcionalidade == 2:
    demo.executar_demo()

elif funcionalidade == 3:

    regras_limites = ("2", "3", "4", "5")
    lista_prole = []
    lista_limites = []

    for chave, valor in ge.regras_pais_dict.items():
        print(f"{chave}: {valor[0]}")
    regra = int(input("Insira o número correspondente à regra desejada: "))
    if regra == 3:
        x, y = input("Insira a quantidade mínima e máxima de pais. Ex: 2 4. :").split()
        regra_pai = ge.regras_pais_dict[regra][1](int(x), int(y))
    else:
        regra_pai = ge.regras_pais_dict[regra][1]
    
    for chave, valor in ge.regras_prole_dict.items():
        print(f"{chave}: {valor[0]}")
    regras = input("Insira os números correspondentes às regras desejadas. Ex: 1 4 5. :").split()

    for i in regras:
        if i not in regras_limites:
            lista_prole.append(ge.regras_prole[int(i)-1][1])
        else:
            n = int(input(f"Insira o <x> referente à regra {ge.regras_prole_dict[int(i)][0]}: "))
            lista_limites.append(ge.regras_prole[int(i)-1][1](n))

    gerador = ge.gerador_arranjo(*lista_prole ,regra_pais=regra_pai, regra_limites=tuple(lista_limites))
    for i in range(10):
        print("Arranjo gerado: ", gerador())
else:
    print("Opção inválida")