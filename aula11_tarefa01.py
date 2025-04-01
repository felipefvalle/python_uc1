"""Exercício 1: Operações Básicas"""

pessoa = {"nome": "Camila" , "idade": 35, "cidade": "Petrópolis"}

print(f"Dados da pessoa: {pessoa}")

pessoa["email"] = "camila@gmail.com"

pessoa["idade"] = 33

del pessoa["cidade"]

pessoa["sexo"] = "femenino"

del pessoa["nome"]
del pessoa["email"]

print("Dados da Pessoa Atualizados.")
print(pessoa)
