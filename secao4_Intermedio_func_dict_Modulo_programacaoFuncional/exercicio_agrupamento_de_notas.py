# 2. Agrupamento de Estudantes por Nota
# Dada uma lista de estudantes com suas respectivas notas, 
# crie um dicionário que agrupe os estudantes pela nota.

import pprint
from itertools import groupby

def Print(v):
    pprint.pprint(v, sort_dicts=False)

estudantes = [
    {'nome': 'Alice', 'nota': 'A'},
    {'nome': 'Bob', 'nota': 'B'},
    {'nome': 'Charlie', 'nota': 'A'},
    {'nome': 'David', 'nota': 'C'},
    {'nome': 'Eve', 'nota': 'B'},
]

def ordem(estudantes):
    return estudantes['nota']

estuudantes_organizados = sorted(estudantes, key= ordem)
grupos = groupby(estuudantes_organizados, key= ordem)
for key, grupo in grupos:
    print('\t\t',key, '\n', '_'*40)
    print(*list(grupo), sep= '\n')


