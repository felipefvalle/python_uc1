numero = int(input("Digite um número: "))

print(f"\nCubos de 1 até {numero}")

for i in range(1, numero + 1):
    print(f"{i}³ = {i ** 3}")
