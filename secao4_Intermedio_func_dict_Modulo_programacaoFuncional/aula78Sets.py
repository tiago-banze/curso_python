# Sets - Conjuntos em Python (tipo set)
# Conjuntos são ensinados na matemática
# https://brasilescola.uol.com.br/matematica/conjunto.htm
# Representados graficamente pelo diagrama de Venn
# Sets em Python são mutáveis, porém aceitam apenas 
# tipos imutáveis como valor interno.


# Criando um set
# set(iterável) ou {1, 2, 3}
# s1 = set('Luiz')
# s1 = set()  # vazios
# s1 = {'Luiz', 1, 2, 3, 3,2,'Luiz',}  # com dados
# print(s1)

# Sets são eficientes para remover valores duplicados
# de iteráveis.
# - Não aceitam valores mutáveis;
# - Seus valores serão sempre únicos;
# - não tem índexes;
# - não garantem ordem;
# - são iteráveis (for, in, not in)
# lista1 = [2,1,2,2,3,3,3,3,3,1,('tiago','Banze')]
# print(lista1)
# set1= set(lista1)
# print(set1)
# lista_sem_nrs_duplicados = list(set1)
# print(lista_sem_nrs_duplicados)
# s1= {1,2,3}
# print(1 not in s1)
# for i in s1:
#     print(i)
# print(len(s1))

# Métodos úteis:
# add, update, clear, discard/remove
s1 = set()
s1.add(2)
# print(s1)
s1.update(('tiago',1,2,3))
# print(s1)
# s1.clear()
s1.discard(9) # não da erro de KeyError quando o elemento que pretende-se descartar não existir
s1.remove(1) # vai dar erro de KeyError quando o elemento que pretende-se descartar não existir
# print(s1)

# Operadores úteis:
# união | união (union) - Une
# intersecção & (intersection) - Itens presentes em ambos
# diferença - Itens presentes apenas no set da esquerda
# diferença simétrica ^ - Itens que não estão em ambos
set1 = {1,2,3}
set2 = {2,3,4}
uniao = set1 | set2
intersecao = set1 & set2
diferente = set1 - set2
diferenca_simetrica = set1 ^ set2
print(f'União :', uniao)
print(f'Intersecão: {intersecao}')
print(f'A diferente B: {diferente}')
print(f"diferenca: {diferenca_simetrica}")