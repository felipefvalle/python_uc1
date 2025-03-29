"""Aula 10 - Atividade 01"""

"""Definindo a Matriz"""

matriz = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
        ]

"""Criando e Exibindo uma Matriz"""

def vetor():
    vetor = [1, 2, 3, 4, 5]
    print("Vetor:", vetor)

    print("Primeiro elemento:", vetor[0]) 
    print("Último elemento:", vetor[-1])  

"""Matriz 4x4"""

matriz_4_4 = [
    
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16],
    ]

"""Utilizando Laço de Repetição For - Adicionando Pipes"""

def pipe():
    for linha in matriz:
        print(f"|", end= "")
        for elemento in linha:
            print(elemento, end='|')
        print()

"""Utilizando For e Input para formar uma Matriz 4x4"""

def matriz_input():
    matriz=[]
    for i in range(4):
        linha = []
        for j in range(4):
            valor = int(input(f"Digite o valor para [{i}] e [{j}]: "))
            linha.append(valor)
        matriz.append(linha)    
    for linha in matriz:
        print(linha)

"""Soma dos Elementos Acima da Diagonal"""

def somatorio():
    soma = 0
    for i in range(4):
            for j in range(4):
                soma = soma + matriz_4_4[i][j]
    print(f"Soma dos elementos acima da diagonal principal: {soma}")

"""Soma dos Elemenos de usando sum"""

def somatorio_sum():
    soma= 0
    for i in range(4):
        soma = soma + sum(matriz_4_4[i])
    print(f"Soma dos elementos acima da diagonal principal: {soma}")

"""Soma dos Elementos usando sum versão 2"""

def somatorio2():
    soma = 0 
    for linha in matriz_4_4:
        soma = soma + sum (linha)
    print(f"Soma dos elementos acima da diagonal principal: {soma}")

"""Soma dos Elementos usando sum versão 3"""

def somatorio3():
    soma = 0
    for indice_linha in range(4):
        soma = soma + sum (indice_linha)
    print(f"Soma dos elementos acima da diagonal principal: {soma}")

"""Soma dos Elementos da Diagonal Secundária"""

def somatorio_secundaria():
    soma = 0
    for i in range(4):
        soma += matriz_4_4[i][3 - i]

    print(f"Soma da diagonal secundária: {soma}")

"""Definindo Maior Valor da Matriz"""

def maior_valor():

    for i in range(4):
        maior = matriz_4_4[i][0]
        for j in range(4):
            if matriz_4_4[i][j] > maior:
                maior = matriz_4_4[i][j]

        print(f"O maior valor da linha: {i}: {maior}")

"""Contagem de Números Pares"""

def pares():
    pares = 0 
    for i in range(4):
        for j in range(4):
            if matriz_4_4[i][j] % 2 == 0:
                pares += 1
    print(f"Quantidade de números pares: {pares}")

"""Contagem de Números Pares e Impares"""

def pares2():
    vet_pares = []
    vet_impares = []
    impares = 0
    pares = 0 
    for i in range(4):
        for j in range(4):
            if matriz_4_4[i][j] % 2 == 0:
                vet_pares.append(matriz_4_4[i][j])
                pares += 1
            else:
                impares = impares + 1 
                vet_impares.append(matriz_4_4[i][j])

    print(f"Quantidade de números pares: {pares}")
    print(f"Quantidade de números impares: {impares}")
    print(f"Os números pares são: {vet_pares}")
    print(f"Os números impares são: {vet_impares}")

def multiplicacao():
    numero = int(input("Digite o número para multiplicação: "))
    linha_escolhida = int(input("Digite a linha a ser multiplicada (0,3): "))
    
    linha=matriz_4_4[linha_escolhida]

    for posicao in range(4):
        linha[posicao] = linha[posicao] * numero

    print(f"Matriz resultante da multiplicação: {linha}")
    

#vetor()
#pipe()
#matriz_input()
#somatorio()
#somatorio_sum()
#somatorio2()
#somatorio3()
#somatorio_secundaria()
#maior_valor()
#matriz_input()
#pares()
#pares2()
#multiplicacao()
