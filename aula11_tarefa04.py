"""Exercício 4: Sistema de Banco de Dados de Alunos"""

aluno1 ={"nome": "Anderson", "notas":[4, 6, 7, 5]}
aluno2 ={"nome": "Erick", "notas": [ 5, 7, 5, 8]}
aluno3 ={"nome": "Luis", "notas": [8, 9, 5, 10]}

print(f"Dados do aluno {aluno1}")

print(f'As notas do aluno {aluno1["nome"]} são {aluno1["notas"]}')

media = sum (aluno1["notas"]) / len (aluno1["notas"])

print(f'O aluno {aluno1["nome"]} obteve a média igual a de {media}')

aluno1["media"] = media

print(f"Dados do aluno {aluno1}")
