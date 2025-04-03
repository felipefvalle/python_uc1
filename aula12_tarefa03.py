class Conta:

    def __init__(self, numero_conta, nome_titular, saldo, limite):
        self.numero_conta = numero_conta
        self.nome_titular = nome_titular
        self.saldo = saldo
        self.limite = limite
    
    def deposito(self, valor):
        print(f"\nSaldo Inicial: {self.saldo}")
        self.saldo = self.saldo + valor
        print(f"Você fez um deposito de {valor}")
        print(f"Saldo Atual: {self.saldo}")

    def saque(self, valor):
        # if valor > self.limite:
        #     return print("Saque Indisponivel - Você não possui limite.")
        print(f"Saldo Inicial: {self.saldo}")
        self.saldo = self.saldo - valor
        print(f"Você realizou um saque de {valor}")
        print(f"Saldo Atual: {self.saldo}")
        
    def exibir_info(self):
        print(f"Conta: {self.numero_conta}\nNome do Titular: {self.nome_titular}\nSaldo: {self.saldo}")

class Banco:
    def __init__(self):
        self.contas = {}

if __name__ == "__main__":
    print(f"\nCriando a primeira conta.")
    print()
    cc1 = Conta("8485", "Felipe", 1500.20, 2000)
    cc1.exibir_info()
    print()
    valordepositado = float(input("Digite o valor do depósito: "))
    cc1.deposito(valordepositado)
    print()
    saque1 = float(input("Digite o valor do saque: "))
    cc1.saque(saque1)
    print()
