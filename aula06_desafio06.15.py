for i in range(1, 21):
    if i % 3 == 0 and i % 5 == 0:
        print(f"{i} é múltiplo de 3 e 5")
    elif i % 3 == 0:
        print(f"{i} é múltiplo de 3")
    elif i % 5 == 0:
        print(f"{i} é múltiplo de 5")
    else:
        print(f"{i} não é múltiplo nem de 3 nem de 5")
