a = float(input("Digite o 1º valor: "))
b = float(input("Digite o 2º valor: "))
c = float(input("Digite o 3º valor: "))

delta = b**2 - 4*a*c

if delta < 0:
    print("não existe resposta")
else:
    x1 = (-b + delta**1/2) / 2*a 
    x2 = (-b - delta**1/2) / 2*a
    print(x1)
    print(x2)
