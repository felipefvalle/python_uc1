numero_secreto = 7

print("Bem-vindo ao jogo de adivinhar o número!")

while True:
    palpite = int(input("Tente adivinhar o número secreto (entre 5 e 10): "))

    if palpite == numero_secreto:
        print("Parabéns! Você acertou!")
        break
    else:
        print("Errado! Tente novamente.")
