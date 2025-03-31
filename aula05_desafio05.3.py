nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
pais = input("Está acompanhado dos pais? <s/n>").lower
lista_banidos = {"joão", "maria", "carlos"}

if (idade >= 18) and (pais == "n"):
    print("Entrada permitida")
elif (idade <= 18) and (pais == "s"):
    print("Entrada permitida.")
else :
    print("Entrada negada.")
