import copy

# dicionario orignal
pessoa = {
    'nome': 'Tiago victor',
    'sobrenome': 'Banze',
    'idade': 25,
    'altura': 1.6,
    'endereco': {
        'rua': 'Av. Principal',
        'numero': 123,
    }
}

# Shallow Copy (Cópia rasa)
pessoa_shallow = copy.copy(pessoa)

# Deep Copy (Cópia profunda)
pessoa_deep = copy.deepcopy(pessoa)
# Modificando o endereço na cópia rasa
pessoa_shallow['endereco']['rua'] = 'Rua Secundária'
# Modificando o endereço na cópia profunda
pessoa_deep['endereco']['rua'] = 'Rua Independente'
# Exibindo os resultados
print("Dicionário original (pessoa):", pessoa)
print("Dicionário com shallow copy (pessoa_shallow):", pessoa_shallow)
print("Dicionário com deep copy (pessoa_deep):", pessoa_deep)