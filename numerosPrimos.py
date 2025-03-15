numero = 1000


for i in range(2,numero+1):
    contador = 0
    for j in range(1,numero+1):
        if i%j == 0:
            contador += 1
    if contador == 2:
        print(i)
        
numeros_primos = [i for i in range(2,10) for j in range(1,10)]
