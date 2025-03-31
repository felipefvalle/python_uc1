numero_secreto = 7
tentativas = 3

print("Tente adivinhar o número entre 1 e 10. Você tem 3 tentativas!")

for tentativa in range(1, tentativas + 1):
    palpite = int(input(f"Tentativa {tentativa}: Digite seu palpite: "))
    
    if palpite == numero_secreto:
        print("Parabéns! Você acertou o número.")
        break
    else:
        print(f"Fim de jogo! O número era {numero_secreto}.")
