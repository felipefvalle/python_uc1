soma = 0  

while True:  
    num = int(input("Digite um número positivo (ou um número negativo para sair): "))
    
    if num < 0:  
        break
    
    soma += num  

print(f"A soma dos números positivos digitados é: {soma}")
