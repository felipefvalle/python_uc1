num = int(input("Digite um número para ver a sua tabuada: "))

print(f"\nTabuada do {num}:")
for i in range(1, 11):  
    print(f"{num} x {i} = {num * i}")  
