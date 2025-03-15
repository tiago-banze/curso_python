# Calculadora de juros para empréstimos

def criar_calculadora_juros(taxa_juros):
    def calcular_juros(valor_principal):
        return valor_principal * (1 + taxa_juros)
    return calcular_juros

# Criando calculadoras para diferentes taxas de juros
juros_baixos = criar_calculadora_juros(0.05)
juros_altos = criar_calculadora_juros(0.15)

# Usando as calculadoras
print(juros_baixos(1000))  
print(juros_altos(1000))   
