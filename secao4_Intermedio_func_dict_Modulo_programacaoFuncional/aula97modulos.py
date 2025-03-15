# Modularização - Entendendo os seus próprios módulos Python
# O primeiro módulo executado chama-se __main__
# Você pode importar outro módulo inteiro ou parte do módulo
# O python conhece a pasta onde o __main__ está e as pastas
# abaixo dele.
# Ele não reconhece pastas e módulos acima do __main__ por
# padrão
# O python conhece todos os módulos e pacotes presentes
# nos caminhos de sys.path
import aula97_m
import sys

# gerar=aula97_m.gerador(aula97_m.lista)
# try:
#     print(next(gerar))
#     print(next(gerar))
#     print(next(gerar))
#     print(next(gerar))
#     print(next(gerar))
#     print(next(gerar))
#     print(next(gerar))
#     print(next(gerar))
#     print(next(gerar))
#     print(next(gerar))
#     print(next(gerar))
# except StopIteration as stopt:
#     print(f'ERRO: Já não tem dados por iterar')
#     print(f'Tipo de ERRO: {stopt.__class__.__name__}')
# print('este modulo chama-se ', __name__)
print()
sys.path.append('caminho')
print(*sys.path, sep='\n')