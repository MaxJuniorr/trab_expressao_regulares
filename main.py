from src.checa_campos_form import checa_campos_form
import src.arranjos_familiares.gerador_arranjos as ge
import src.arranjos_familiares.checa_arranjos_familiares as ch
import random

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
elif funcionalidade == 2:
    regra_a1 = ge.gerador_arranjo(regra_limites=(ge.floor_m,),int_params=(2,),regra_pais=ge.criar_casais_hetero)
    regra_a2 = ge.gerador_arranjo(regra_limites=(ge.floor_h,),int_params=(1,),regra_pais=ge.criar_casais_hetero)
    regra_a3 = ge.gerador_arranjo(regra_limites=(ge.floor_h, ge.floor_m),int_params=(2, 1),regra_pais=ge.criar_casais_hetero)

    letra_a = ge.disjuncao(regra_a1, regra_a2, regra_a3)
    letra_a.__name__ = "letra_a"

    letra_b = ge.gerador_arranjo(ge.impar_m ,regra_pais=ge.criar_casais_hetero)
    letra_b.__name__ = "letra_b"
    letra_c = ge.gerador_arranjo(ge.mais_velho_m, ge.mais_novo_h ,regra_pais=ge.criar_casais_hetero)
    letra_c.__name__ = "letra_c"
    letra_d = ge.gerador_arranjo(ge.floor6_prole, ge.casal_primeiro, ge.casal_ultimo ,regra_pais=ge.criar_casais_homo)
    letra_d.__name__ = "letra d"
    letra_e = ge.gerador_arranjo(ge.filhos_alternados ,regra_pais=ge.criar_casais_homo)
    letra_e.__name__ = "letra e"
    letra_f = ge.gerador_arranjo(ge.nao_filhos_h_consecutivos ,regra_pais=ge.criar_casais_homo)
    letra_f.__name__ = "letra f"
    letra_g = lambda: print("doido")
    letra_g.__name__ = "letra g"

    opcoes = {
        "1": (letra_a, ch.validar_arranjo_alfa),
        "2": (letra_b, ch.validar_arranjo_beta),
        "3": (letra_c, ch.validar_arranjo_charlie),
        "4": (letra_d, ch.validar_arranjo_delta),
        "5": (letra_e, ch.validar_arranjo_echo),
        "6": (letra_f, ch.validar_arranjo_foxtrot),
        "7": (letra_g, ch.validar_arranjo_golf)
    }




    print("Escolha uma opção: ")
    for numero, opcao in opcoes.items():
        print(f"{numero} - {opcao[0].__name__}")
    
    numero = input("Número escolhido: ")

    if numero == "7":
        x = int(input("Insira o valor de x: "))
        y = int(input("Insira o valor de y: "))
        letra_g = ge.gerador_arranjo(ge.nao_ultimos3_h_consecutivos ,regra_pais=ge.criar_nsais_platonico(x, y))
        cadeia = letra_g()        
        print("Cadeia gerada: ", cadeia)
        print("Verificando cadeia gerada: ", "Cadeia aceita!" if ch.validar_arranjo_golf(cadeia, x, y) else "Cadeia recusada!")
    else:
        escolha = opcoes[numero][0]
        cadeia = escolha()
        print("Cadeia gerada: ", cadeia)
        print("Verificando cadeia gerada: ", "Cadeia aceita!" if opcoes[numero][1](cadeia) else "Cadeia recusada!")

    # teste de força para caso ainda queria testar (deve ser apagado no final do projeto)
    # print("=TESTE DE FORÇA=")
    # for i in range(1000000):
    #     cadeia = letra_d()
    #     teste = "Cadeia aceita!" if ch.validar_arranjo_delta(cadeia) else "Cadeia recusada!"
    #     if teste == "Cadeia recusada!":
    #         print("Cadeia gerada: ", cadeia)
    #         print("Verificando cadeia gerada: ", teste)
    #         break

else:
    print("Opção inválida")
