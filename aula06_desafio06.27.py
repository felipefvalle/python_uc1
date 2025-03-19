a, b = 0, 1  
contador = 0  

print("Sequência de Fibonacci:")

while contador < 10:
    print(a, end=" ")
    a, b = b, a + b  
    contador += 1
