"""
Lista de listas e seus índices
"""

sala = [['Maria','Helena',], ['Elaine',], ['Luiz', 'João', 'Eduardo',],"tiago"]
i=0

# for i,valor in enumerate(sala):
#     print(f'\t\tsala [{i+1}]')
#     print('___________________________________________')
#     for item in sala[i]:
#         print(f'\t*{item}')
#     print('\n')
for salas in sala:
    i=i+1
    print(f'\t\tsala [{i}]')
    print('___________________________________________')
    for aluno in salas:
        print(f'\t*{aluno}')
print(sala[0][1])