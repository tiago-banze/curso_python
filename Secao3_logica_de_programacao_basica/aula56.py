"""
split e join com list e str
split - divide uma string
join - une uma string
"""
frase = "Olha só que, coisa interessante!     "
lista_de_frases = frase.split(",")
for i, frase in enumerate(lista_de_frases):
    print(lista_de_frases[i].strip())
print(lista_de_frases)
frases_unidas= ','.join(lista_de_frases)
print(frases_unidas)