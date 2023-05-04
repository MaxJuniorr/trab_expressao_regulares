import src.arranjos_familiares.gerador_arranjos as ge
import src.arranjos_familiares.checa_arranjos_familiares as ch
import os

def executar_demo() -> None:
    regra_a1 = ge.gerador_arranjo(regra_limites=(ge.floor_m_out(2),), regra_pais=ge.criar_casais_hetero)
    regra_a2 = ge.gerador_arranjo(regra_limites=(ge.floor_h_out(1),), regra_pais=ge.criar_casais_hetero)
    regra_a3 = ge.gerador_arranjo(regra_limites=(ge.floor_h_out(2), ge.floor_m_out(1)), regra_pais=ge.criar_casais_hetero)

    letra_a = ge.disjuncao(regra_a1, regra_a2, regra_a3)
    letra_a.__name__ = "a)"
    letra_b = ge.gerador_arranjo(ge.impar_m, regra_pais=ge.criar_casais_hetero)
    letra_b.__name__ = "b)"
    letra_c = ge.gerador_arranjo(ge.mais_velho_m, ge.mais_novo_h, regra_pais=ge.criar_casais_hetero)
    letra_c.__name__ = "c)"
    letra_d = ge.gerador_arranjo(ge.floor6_prole, ge.casal_primeiro, ge.casal_ultimo, regra_pais=ge.criar_casais_homo)
    letra_d.__name__ = "d)"
    letra_e = ge.gerador_arranjo(ge.filhos_alternados, regra_pais=ge.criar_casais_homo)
    letra_e.__name__ = "e)"
    letra_f = ge.gerador_arranjo(ge.nao_filhos_h_consecutivos, regra_pais=ge.criar_casais_homo)
    letra_f.__name__ = "f)"
    letra_g = lambda: print("doido")
    letra_g.__name__ = "g)"

    opcoes = {
        "1": (letra_a, ch.validar_arranjo_alfa),
        "2": (letra_b, ch.validar_arranjo_beta),
        "3": (letra_c, ch.validar_arranjo_charlie),
        "4": (letra_d, ch.validar_arranjo_delta),
        "5": (letra_e, ch.validar_arranjo_echo),
        "6": (letra_f, ch.validar_arranjo_foxtrot),
        "7": (letra_g, ch.validar_arranjo_golf)
    }

    n = "3"
    while n == "3":
        os.system("clear")
        print("""
            _________________________________________  
            ((                                     ))
            )) Trabalho sobre expressões regulares (( 
            ((                                     ))
            -----------------------------------------  
        
    --> Gerar arranjos familiares (Demonstração da 2ª questão)
        """)
        print("""OPÇÕES:

Nº - DESCRIÇÃO""")
        for numero, opcao in opcoes.items():
            print(f"{numero}  - {opcao[0].__name__} {opcao[1].__doc__.split('.')[0]}.")
        
        numero = input("\nEscolha uma opção para prosseguir.\nNº: ")


        if numero in opcoes.keys():
            n = "2"
            while n == "2":
                os.system("clear")
                print(f"""
            _________________________________________  
            ((                                     ))
            )) Trabalho sobre expressões regulares (( 
            ((                                     ))
            -----------------------------------------  
        
    --> Gerar arranjos familiares (Demonstração da 2ª questão)
    --> Regra: {opcoes[numero][1].__doc__.split('.')[0]}.
                """)
                alternativa = input("""Selecione uma das opções abaixo:
                1 - Gerar uma cadeia aleatória conforme a regra.
                2 - Validar cadeia conforme a regra.
                Nº: """)
                if alternativa == "1":
                    if numero == "7":
                        x, y = input("Insira a quantidade mínima e máxima de pais. Ex: 2 4. :").split()
                        letra_g = ge.gerador_arranjo(ge.nao_ultimos3_h_consecutivos, regra_pais=ge.criar_nsais_platonico(int(x), int(y)))
                        
                        n = "1"
                        while n == "1":
                            os.system("clear")
                            print(f"""
            _________________________________________  
            ((                                     ))
            )) Trabalho sobre expressões regulares (( 
            ((                                     ))
            -----------------------------------------  
        
    --> Gerar arranjos familiares (Demonstração da 2ª questão)
    --> Regra: {opcoes[numero][1].__doc__.split('.')[0]}.
    --> Gerar uma cadeia aleatória conforme a regra.
                            """)


                            print("Cadeia gerada: ", letra_g())
                            
                            n = "6"
                            while n not in ("1", "2", "3", "4", "5"):
                                n = input("""
                OPÇÕES:
                1 - Gerar outra cadeia aleatória
                2 - Escolher outra opção
                3 - Selecionar outra regra
                4 - Voltar ao menu principal
                
                Nº: """)
                    else:

                        n = "1"
                        while n == "1":
                            os.system("clear")
                            print(f"""
            _________________________________________  
            ((                                     ))
            )) Trabalho sobre expressões regulares (( 
            ((                                     ))
            -----------------------------------------  
        
    --> Gerar arranjos familiares (Demonstração da 2ª questão)
    --> Regra: {opcoes[numero][1].__doc__.split('.')[0]}.
    --> Gerar uma cadeia aleatória conforme a regra.
                            """)

                            print("Cadeia gerada: ", opcoes[numero][0]())

                            n = "6"
                            while n not in ("1", "2", "3", "4", "5"):
                                n = input("""
                OPÇÕES:
                1 - Gerar outra cadeia aleatória
                2 - Escolher outra opção
                3 - Selecionar outra regra
                4 - Voltar ao menu principal
                
                Nº: """)

                        
                elif alternativa == "2":
                    if numero == "7":
                        n = "1"
                        while n == "1":
                            os.system("clear")
                            print(f"""
            _________________________________________  
            ((                                     ))
            )) Trabalho sobre expressões regulares (( 
            ((                                     ))
            -----------------------------------------  
        
    --> Gerar arranjos familiares (Demonstração da 2ª questão)
    --> Regra: {opcoes[numero][1].__doc__.split('.')[0]}.
    --> Validar cadeia conforme a regra.
                            """)


                            x, y = input("Insira a quantidade mínima e máxima de pais. Ex: 2 4. :").split()
                            cadeia = input("Insira a cadeia a ser validada: ")
                            print("\nA cadeia inserida é ", "válida!" if ch.validar_arranjo_golf(cadeia, x, y) else "inválida!")
                            
                            n = "6"
                            while n not in ("1", "2", "3", "4", "5"):
                                n = input("""
                OPÇÕES:
                1 - Validar outra cadeia
                2 - Escolher outra opção
                3 - Selecionar outra regra
                4 - Voltar ao menu principal
                
                Nº: """)
                    else:

                        n = "1"
                        while n == "1":
                            os.system("clear")
                            print(f"""
            _________________________________________  
            ((                                     ))
            )) Trabalho sobre expressões regulares (( 
            ((                                     ))
            -----------------------------------------  
        
    --> Gerar arranjos familiares (Demonstração da 2ª questão)
    --> Regra: {opcoes[numero][1].__doc__.split('.')[0]}.
    --> Validar cadeia conforme a regra.
                            """)


                            cadeia = input("Insira a cadeia a ser validada: ")
                            print("\nA cadeia inserida é ", "válida!" if opcoes[numero][1](cadeia) else "inválida!")
                            
                            n = "6"
                            while n not in ("1", "2", "3", "4", "5"):
                                n = input("""
                OPÇÕES:
                1 - Validar outra cadeia
                2 - Escolher outra opção
                3 - Selecionar outra regra
                4 - Voltar ao menu principal
                
                Nº: """)

                else:
                    input("\nOpção inválida! Por favor, tente novamente.\nPressione ENTER para continuar.")
        else:
            input("\nOpção inválida! Por favor, tente novamente.\nPressione ENTER para continuar.")
