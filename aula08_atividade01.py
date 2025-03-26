def saudacao():
    print("Seja bem-vindo ao curso de Python!")

def soma(a, b):
    return a + b
def teste_soma():
    resultado = soma(8, 2)
    print(f"O resultado da soma é {resultado}")



def fatorial(n):
    if n < 0:
        return "Número inválido para fatorial."
    elif n == 0:
            return 1 
    else:
        resultado = 1 
        for i in range (1 , n + 1):
            resultado *= i 
        return resultado 

def testar_fatorial():
    n = int(input("Informe um número: "))
    resultado = fatorial(n)
    print(f"\n\n\tO fatorial do numero {n} é: {resultado}\n\n")


if __name__ == "__main__":
    testar_fatorial()
