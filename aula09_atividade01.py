
"""
Aula 09 - Atividade 01
"""

vetor_dados = [10, 20, 30, 40, 50]
vetor_dados2 = [1, 2, 3, 4, 5]
vetor_dados3 = [9, 7, 5, 8, 6, 4]
vetor_dados4 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
vetor_dados5 = [5, 5, 5, 5, 5]

"""Criar e Imprimir uma Lista"""

def imprimir_lista(vetor):
    print("\n\tImprimindo Conteudo do Vetor.")
    print(f"\nO conteudo do vetor é {vetor}\n")

"""Iterando a lista"""

def iterando_lista(vetor):
    for elemento in vetor:
        print("\n\tIterando a Lista")
        print("\nO conteudo do elemento é: ", elemento) 
        

"""Utilizando NumPy para Operações com Vetores"""

#def numpy_vet(vetor):
    #vetor_np = np.array([1, 2, 3, 4, 5])
    #print("Vetor com NumPy: ", vetor_np)

"""Somar os Elementos do Vetor"""

def soma(vetor):
    soma = sum(vetor)
    print("\n\tSomando os Elementos do Vetor")
    print("\nSoma dos elementos:", soma)
    print("\n")

"""Encontrar o Maior e Menos Valor"""

def maior_e_menor(vetor):
    maior = max(vetor)
    menor = min(vetor)

    print("\n\tEncontrando o Maior e Menor Valor.")
    print("\nMaior valor:", maior)
    print("Menor valor: ", menor)
    print("\n")

"""Inverter os Elementos do Vetor sem Usar o reverse()"""

def inverdito(velor):
    vetor_invertido = vetor[::-1]
    print("\n\tInverter os Elementos do Vetor")
    print("\nValor invertido é: ", vetor_invertido)
    print("\n")

"""Multiplicar Cada Elemento por 2 e Amarzenar em um Novo Vetor"""

def multiplicacao(vetor):
    multiplicador = 2 
    vetor_mult = [elemento * multiplicador for elemento in vetor]
    print("\n\tMultiplicando Cada Elemento por 2 e Amarzenando em um Novo Vetor")
    print("\nO resultado do vetor multiplicado é: ", vetor_mult)
    print("\n")

"""Contar Quantas Vezes o Valor 5 Aparece no Vetor"""

def vezes(vetor):
    ocorrencias = vetor.count(5)
    print("\n\tContar Quantas Vezes o Valor 5 Aparece")
    print("\nO valor 5 aparece", ocorrencias, "vezes.")
    print("\n")

""""Ordernar um Vetor em Ordem Crescente"""

def ordernar(vetor):
    vetor_ordenado = sorted(vetor)
    print("\n\tOrdernando o Vetor em Ordem Crescente.")
    print("\nO vetor ordenado ", vetor_ordenado)
    print("\n")

"""Remover Elementos Duplicados no Vetor"""

def remover_elementos_duplicados(vetor):
    vetor_sem_diplicadas = list(dict.fromkeys(vetor))
    print("\n\tRemovendo Elementos Duplicados")
    print("\n Vetor sem duplicatas é: ", vetor_sem_diplicadas)
    print("\n")

"""Separando Pares e Impares"""

def impares_pares(vetor):
    pares = [num for num in vetor if num % 2== 0]
    impares = [num for num in vetor if num % 2 != 0 ]
    print("\n\tSeparando Números Impares e Pares.")
    print("\nPares:", pares)
    print("\nImpares:", impares)
    print("\n")

"""Calcular a Média e Exibir Elementos Acima da Média"""

def media(vetor):
    media = sum(vetor) / len(vetor)
    acima_media = [num for num in vetor if num > media]
    print("\n\tCalculando a Média do vetor.")
    print("\nMedia:", media)
    print("Elementos acima da média:", acima_media)
    print("\n")

if __name__ == "__main__":
    """Imprimir e Criar Lista"""
    imprimir_lista(vetor_dados)
    """Iterando a Lista"""
    iterando_lista(vetor_dados)
    """Calculando a Soma dos Elementos"""
    soma(vetor_dados)
    """Maior e Menor Valor"""
    maior_e_menor(vetor_dados)
    """Multiplicador dos Elementos"""
    multiplicacao(vetor_dados3)
    """Contar Quantas Vezes o Valor 5 Aparece no Vetor"""
    vezes(vetor_dados5)
    """Ordernar o Vetor em Ordem Crescente"""
    ordernar(vetor_dados3)
    """Separando Pares e Impares"""
    impares_pares(vetor_dados2)
    """calcular a Média e Exibir Elementos Acima da Média"""
    media(vetor_dados2)
