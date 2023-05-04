from src.checa_campos_form import checa_campos_form
import src.arranjos_familiares.gerador_arranjos as ge
from src import demo
import os

n = "3"
while n == "3":
    os.system("clear")
    print("""
            _________________________________________  
            ((                                     ))
            )) Trabalho sobre expressões regulares (( 
            ((                                     ))
            -----------------------------------------  
    """)
        
    print("""FUNCIONALIDADES:

    Nº - FUNCIONALIDADE
    1  - Máscara de validação de campos de um formulário
    2  - Gerar arranjos familiares (Demonstração da 2ª questão)
    3  - Gerar arranjos familiares (Implementação customizável)

    (qualquer outra tecla + enter - encerrar o programa)
    """)

    funcionalidade = input("Escolha uma funcionalidade para prosseguir.\n"
                            "Nº: ")

    if funcionalidade == "1":
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
        n = "2"
        while n == "2":
            os.system("clear")
            print("""
            _________________________________________  
            ((                                     ))
            )) Trabalho sobre expressões regulares (( 
            ((                                     ))
            -----------------------------------------  
        
    --> Máscara de validação de campos de um formulário
            """)
            print("""FUNCIONALIDADES:

Nº - FUNCIONALIDADE""")
            for numero, opcao in opcoes.items():
                print(f"{numero}  - {opcao.__name__}")
            func = input("\nEscolha uma funcionalidade para proceguir.\n"
                                    "Nº: ")
            if func in opcoes.keys():

                escolha = opcoes[func]
                n = "1"
                while n == "1":
                    os.system("clear")
                    print(f"""
            _________________________________________  
            ((                                     ))
            )) Trabalho sobre expressões regulares (( 
            ((                                     ))
            -----------------------------------------  
        
    --> Máscara de validação de campos de um formulário
    --> {escolha.__name__}
                    """)

                    print(escolha.__doc__)
                    entrada = input("Cadeia: ")
                    resultado = escolha(entrada)

                    os.system("clear")
                    print(f"""
            _________________________________________  
            ((                                     ))
            )) Trabalho sobre expressões regulares (( 
            ((                                     ))
            -----------------------------------------  
        
    --> Máscara de validação de campos de um formulário
        --> {escolha.__name__}
                    """)

                    print(f"A cadeia '{entrada}' é {'valida!' if resultado else 'invalida!'}")

                    n = "5"
                    while n not in ("1", "2", "3", "4"):
                        n = input("""
                OPÇÕES:
                1 - Testar outra cadeia
                2 - Escolher outra funcionalidade
                3 - Voltar ao menu principal
                4 - Sair
                
                Nº: """)
                        if n not in ("1", "2", "3", "4"):
                            os.system("clear")
                            print(f"""
            _________________________________________  
            ((                                     ))
            )) Trabalho sobre expressões regulares (( 
            ((                                     ))
            -----------------------------------------  
        
    --> Máscara de validação de campos de um formulário
        --> {escolha.__name__}
                            """)
                            print("Opção inválida! Por favor, tente novamente.")
            else:
                input("\nOpção inválida! Por favor, tente novamente.\nPressione ENTER para continuar.")
    elif funcionalidade == "2":
        demo.executar_demo()

    elif funcionalidade == "3":
        atencao = """\nATENÇÃO: Esta funcionalidade é experimental e pode não funcionar corretamente.
    Combinar regras de maneira ilógica pode gerar absurdos ou loops infinitos.
    Algumas combinações de regras flagrantemente antagônicas não são permitidas.
    Para mais informações, consulte o arquivo README.md
    """
        n = "2"
        while n == "2":
            os.system("clear")
            print(atencao)
            print("""
            _________________________________________  
            ((                                     ))
            )) Trabalho sobre expressões regulares (( 
            ((                                     ))
            -----------------------------------------  
        
    --> Máscara de validação de campos de um formulário
            """)

            regras_limites = ("2", "3", "4", "5")
            lista_prole = []
            lista_limites = []

            print("""REGRA DE PAIS:

Nº - REGRA""")

            for chave, valor in ge.regras_pais_dict.items():
                print(f"{chave}  - {valor[0]}")
            
            regra = input("\nInforme o número da regra desejada para prosseguir.\n"
                                "Nº: ")
            
            if regra in ["1", "2", "3"]:
                regra = int(regra)
                regra_x = regra
                if regra == 3:
                    x, y = input("Insira a quantidade mínima e máxima de pais. Ex: 2 4. :").split()
                    regra_pai = ge.regras_pais_dict[regra][1](int(x), int(y))
                else:
                    regra_pai = ge.regras_pais_dict[regra][1]
                
                os.system("clear")
                print(atencao)
                print(f"""
            _________________________________________  
            ((                                     ))
            )) Trabalho sobre expressões regulares (( 
            ((                                     ))
            -----------------------------------------  
        
    --> Máscara de validação de campos de um formulário
    --> REGRA DE PAIS:
        - {ge.regras_pais_dict[regra_x][0]}
            """)

                print("""REGRA DE PROLE:

Nº - REGRAS""")
                for chave, valor in ge.regras_prole_dict.items():
                    print(f"{chave}  - {valor[0]}")
                
                regras = input("\nInsira os números correspondentes às regras desejadas. Ex: 1 4 5. : ").split()
                proibidas = ge.combinacoes_proibidas.items()

                erro = False
                for regra in proibidas:
                    controle = 0
                    for j in range(2):
                        controle += 1 if str(regra[j]) in regras else 0
                    if controle == 2:
                        erro = True
                        tupla = regra
                        
                if erro:
                    print("Erro: As regras escolhidas não podem ser usadas juntas. ", tupla)
                    exit()
                
                for i in regras:
                    if i not in regras_limites:
                        lista_prole.append(ge.regras_prole[int(i)-1][1])
                    else:
                        n = int(input(f"Insira o <x> referente à regra '{ge.regras_prole_dict[int(i)][0]}': "))
                        lista_limites.append(ge.regras_prole[int(i)-1][1](n))

                gerador = ge.gerador_arranjo(*lista_prole, regra_pais=regra_pai, regra_limites=tuple(lista_limites))

                n = "1"
                while n == "1":
                    os.system("clear")
                    print(atencao)
                    print(f"""
            _________________________________________  
            ((                                     ))
            )) Trabalho sobre expressões regulares (( 
            ((                                     ))
            -----------------------------------------  
        
    --> Máscara de validação de campos de um formulário
    --> REGRA DE PAIS:
        - {ge.regras_pais_dict[regra_x][0]}
    --> REGRA DE PROLE:""")
                    for i in range(len(lista_prole)):
                        print(f"        - {ge.regras_prole_dict[int(regras[i])][0]}")


                    print("\nCadeia gerada: ", gerador())
                    n = "5"
                    while n not in ("1", "2", "3", "4"):
                        n = input("""
                OPÇÕES:
                1 - Gerar outra cadeia com as mesmas regras
                2 - Construir novo gerador
                3 - Voltar ao menu principal
                4 - Sair
                
                Nº: """)
                        if n not in ("1", "2", "3", "4"):
                            input("Opção inválida! Por favor, tente novamente. \nPressione ENTER para continuar.")

            else:
                input("Opção inválida! Por favor, tente novamente. \nPressione ENTER para continuar.")
                input()
    else:
        n = "4"
os.system("clear")
print("""

░█████╗░██████╗░██████╗░██╗░██████╗░░█████╗░██████╗░░█████╗░██╗
██╔══██╗██╔══██╗██╔══██╗██║██╔════╝░██╔══██╗██╔══██╗██╔══██╗██║
██║░░██║██████╦╝██████╔╝██║██║░░██╗░███████║██║░░██║██║░░██║██║
██║░░██║██╔══██╗██╔══██╗██║██║░░╚██╗██╔══██║██║░░██║██║░░██║╚═╝
╚█████╔╝██████╦╝██║░░██║██║╚██████╔╝██║░░██║██████╔╝╚█████╔╝██╗
░╚════╝░╚═════╝░╚═╝░░╚═╝╚═╝░╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝
""")