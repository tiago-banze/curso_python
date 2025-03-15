'''
Fatiamento de strings
 012345678
 Olá Mundo
-987654321

Fatiamento [i:f:p] [::]
onde: i->é o inicio ou de onde começamos a fatiar a string
f->é o fim ou onde queremos parar o fatiamento. normalmento vai mostrar o valor que estiver no indice que estiver antes doque colocamos
p->é passo 

a função len retorna a qtd de caracteres da str
'''
variavel = 'Olá mundo'
print(variavel[2:len(variavel):2])
print(variavel[::-1])