SENHA = "1234"  

while True:  
    digite_senha = input("Digite a senha: ")  
    
    if digite_senha == SENHA:  
        print("Acesso permitido!")
        break  
    else:
        print("Senha incorreta. Tente novamente.")
