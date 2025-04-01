"""Exercício 2: União de Dicionários"""

d3=d1 = {"a": 1, "b": 2}
d2 = {"b": 3, "c": 4}

print("Dicionários Originais.")
print(f"D1  : {d1}")
print(f"D2  : {d2}")

d1.update(d2)
d2.update(d3)

print("Dicionários Atualizados.")
print(f"D1  : {d1}")
print(f"D2  : {d2}")
