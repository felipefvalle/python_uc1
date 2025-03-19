numero = int(input("Digite um número para verificar se é primo: "))

eh_primo = True

for i in range(2,numero):
    if numero % i == 0:
        eh_primo = False
        break

if eh_primo and numero > 1:
    print(f"{numero} é primo!")

else:
    print(f"{numero} não é primo!")
