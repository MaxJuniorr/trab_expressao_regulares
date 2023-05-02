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

    for chave, valor in ge.regras_pais_dict.items():
        print(f"{chave}: {valor[0]}")
    regra_pais = int(input("Insira o número correspondente à regra desejada: "))
    
    for chave, valor in ge.regras_prole_dict.items():
        print(f"{chave}: {valor[0]}")
    regras = input("Insira os números correspondentes às regras desejadas. Ex: 1 4 5. :").split()

    
    lista = [ge.regras_prole[int(i)-1][1] for i in regras]

    gerador = ge.gerador_arranjo(*lista ,regra_pais=ge.regras_pais_dict[regra_pais][1])
    for i in range(10):
        print("Arranjo gerado: ", gerador())
else:
    print("Opção inválida")