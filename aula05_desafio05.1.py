    idade = int(input("Digite sua idade: "))
    if idade < 18:
        print("Acesso negado. Você deve ter mais de 18 anos.")
        return
    
    senha_correta = "senha123"  # Defina a senha correta aqui
    senha = input("Digite a senha: ")
    
    if senha == senha_correta:
        print("Acesso permitido! Bem-vindo.")
    else:
        print("Senha incorreta. Acesso negado.")
