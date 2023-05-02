import src.arranjos_familiares.gerador_arranjos as ge
import src.arranjos_familiares.checa_arranjos_familiares as ch


def executar_demo() -> None:
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

    # [TODO] FORMATAR OUTPUT
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
    elif numero in opcoes.keys():
        escolha = opcoes[numero][0]
        cadeia = escolha()
        print("Cadeia gerada: ", cadeia)
        print("Verificando cadeia gerada: ", "Cadeia aceita!" if opcoes[numero][1](cadeia) else "Cadeia recusada!")
    else:
        print("Opção inválida")