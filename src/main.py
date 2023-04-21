from checa_campos_form import checa_campos_form


nome = checa_campos_form.Nome()
email = checa_campos_form.Email()
senha = checa_campos_form.Senha()
cpf = checa_campos_form.Cpf()
telefone = checa_campos_form.Telefone()
datetime = checa_campos_form.Datetime()
numero = checa_campos_form.Numero()

verificador_de_nome = checa_campos_form.Verificador(nome)
verificador_de_email = checa_campos_form.Verificador(email)
verificador_de_senha = checa_campos_form.Verificador(senha)
verificador_de_cpf = checa_campos_form.Verificador(cpf)
verificador_de_telefone = checa_campos_form.Verificador(telefone)
verificador_de_datetime = checa_campos_form.Verificador(datetime)
verificador_de_numero = checa_campos_form.Verificador(numero)

resultado_email = verificador_de_email.reconhecer("nome@provedor.com.br")
print(resultado_email)