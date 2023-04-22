from checa_campos_form import checa_campos_form


nome = checa_campos_form.Nome()
email = checa_campos_form.Email()
senha = checa_campos_form.Senha()
cpf = checa_campos_form.Cpf()
telefone = checa_campos_form.Telefone()
datetime = checa_campos_form.Datetime()
numero = checa_campos_form.Numero()

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
    print(f"{numero} - {str(opcao)}")
escolha = opcoes[input("Número escolhido: ")]

verificador = checa_campos_form.Verificador(escolha)
entrada = input("Qual o valor a ser verificado? ")
resultado = verificador.reconhecer(entrada)

print(f"{str(escolha)} é {'valido(a)' if resultado else 'invalido(a)'}")