media = float(input("Digite a média do aluno: "))
trabalho_extra = input("O aluno fez o trabalho extra? (s/n): ").lower()

if media >= 7 or trabalho_extra == 's':
    print("Aluno aprovado!")
else:
    print("Aluno reprovado.")
