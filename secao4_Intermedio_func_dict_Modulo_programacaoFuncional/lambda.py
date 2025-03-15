# pessoas = [{'nome': "tiago",'idade':20},
#            {'nome': "andre",'idade':10},
#            {'nome': "julio",'idade':70},
#            {'nome': "castro",'idade':30}]

# def somar(x,y):
#     return x+y

# print(somar(2,8))

# somar_lambda = lambda x,y: x + y
# print(somar_lambda(2,8))

# usamos as funções lambdas porque elas são compactas, elas são escritas em uma linha de codigo.
# ela é vantagioso porque podemos usar ela no momento que criamos,, diferente dos que definimos(def)
# que é necessario definir para depois usar. 

# Podemos usar as funções lambdas quando estivermos a trabalhar com funções de alta ordem
# funcões de alta ordem (hight order function) são aquela que recebem funções como parametros ou função dentro de uma outra função
# exemplo de função de alta ordem é o filter, essa função filtra dados de uma coleção (list, tuple, dict ou set)

#criar um programa que filtra nr maior que 30
lista=[]
numeros = [1,2,3,45,67,3,34,32,31,30,45,6,67,89,0,90,87,56]

# def nr_mais_30(numero):
#     return numero >30
filtro_30= sorted(list( filter(lambda x:x<30,numeros)))
print(filtro_30)
