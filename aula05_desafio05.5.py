nome = input("Digite seu nome: ")
if len(nome) < 3:
    print("Cadastro negado. O nome deve ter pelo menos 3 letras.")

senha = input("Digite sua senha: ")
if len(senha) < 6:
    print("Cadastro negado. A senha deve ter pelo menos 6 caracteres.")

senha_fraca = ['123456', 'senha']
if senha in senha_fraca:
    print("Cadastro negado. A senha é muito fraca.")
else:
    print("Cadastro realizado com sucesso!")
