numero = input("Digite um número: ")

quantiade_digitos = len(numero) if numero.isdigit() else len(numero) - 1 if numero[0] == "-" else len(numero)

print(f"O número {numero} tem {quantiade_digitos} dígitos.")
