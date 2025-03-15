# Exercício 1: Criação e Operações Básicas
# Crie um set chamado frutas contendo as frutas "maçã", "banana", "cereja".
# Adicione a fruta "laranja" ao set.
# Remova a fruta "banana" do set.
# Verifique se "maçã" está presente no set e imprima o resultado.

# frutas=set()
# frutas = {'maçã','banana','cereja'}

# frutas.add('laranja')
# maca_tem = 'maçã' in frutas

# if maca_tem:
#     print(f'maça está presentes no conto frutas')
# print(frutas)


# Exercício 2: Operações de Conjunto
# Crie dois sets: pares com os números 2, 4, 6, 8 e impares com os números 1, 3, 5, 7.
# Encontre e imprima a união dos dois sets.
# Encontre e imprima a interseção dos dois sets.
# Encontre e imprima a diferença entre pares e impares.
# Encontre e imprima a diferença simétrica entre pares e impares.

# conjunto_pares = {2,4,6,8}
# conjunto_impares = {1,3,5,7}
# print(conjunto_pares | conjunto_impares)
# print(conjunto_pares & conjunto_impares)
# print(conjunto_pares - conjunto_impares)
# print(conjunto_pares ^ conjunto_impares)


# Exercício 3: Remoção de Duplicatas
# Dada a lista numeros = [1, 2, 2, 3, 4, 4, 5], crie um set para remover os duplicados.
# Converta o set de volta para uma lista e imprima o resultado.

# numeros = [1,2,2,3,4,4,5]
# nova_lista_numeros = list(set(numeros))
# print(nova_lista_numeros)