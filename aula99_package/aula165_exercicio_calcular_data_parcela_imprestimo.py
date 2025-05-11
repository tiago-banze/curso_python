# Exercício solucionado: calculando as datas e parcelas de um empréstimo
# Maria pegou um empréstimo de 1.000.000
# para realizar o pagamento em 5 anos.
# A data em que ela pegou o empréstimo foi
# 20/12/2020 e o vencimento de cada parcela
# é no dia 20 de cada mês.
# - Crie a data do empréstimo
# - Crie a data do final do empréstimo
# - Mostre todas as datas de vencimento e o valor de cada parcela
from datetime import datetime
from dateutil.relativedelta import relativedelta

emprestimo = 1_000_000
formato_data = '%d / %m / %Y'
data_emprestimo = datetime(day=20,month=12,year=2020)
delta_anos = relativedelta(years=5)
data_final_emprestimo = data_emprestimo + delta_anos


data_parcelas = []
data_parcela = data_emprestimo

while data_parcela < data_final_emprestimo:
    data_parcelas.append(data_parcela)
    data_parcela += relativedelta(months=+1)
    

numro_parcelas = len(data_parcelas)
valor_parcela = emprestimo/ len(data_parcelas)
for data in data_parcelas:
    print(f'{data.strftime('%d/%m/%Y')}, {valor_parcela:,.2f} mt')    
print()
print(
    f'você pegou {emprestimo:,.2f} mt para pagar'
    f'em {delta_anos.years} anos'
    f'({numro_parcelas} meses) em parcelas de '
    f'{valor_parcela:,.2f}.'
)
