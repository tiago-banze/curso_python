# Criando datas com módulo datetime
# datetime(ano, mês, dia)
# datetime(ano, mês, dia, horas, minutos, segundos)
# datetime.strptime('DATA', 'FORMATO')
# datetime.now()
# https://pt.wikipedia.org/wiki/Era_Unix
# datetime.fromtimestamp(Unix Timestamp)
# https://docs.python.org/3/library/datetime.html
# Para timezones
# https://en.wikipedia.org/wiki/List_of_tz_database_time_zones
# Instalando o pytz
# pip install pytz types-pytz
from datetime import datetime
from pytz import timezone, all_timezones

# data_str_data = '2022/04/20 07:49:23'
# data_str_data = '20/04/2025'
# data_str_fmt = '%d/%m/%Y'
# # data_str_fmt = '%d/%m/%Y %H:%M:%S'
# data = datetime.strptime(data_str_data, data_str_fmt)
# # data = datetime(2022, 4, 20,23)
# print(data)
fuso_am = timezone("Africa/Maputo")
data_am = datetime.now(fuso_am)


print(f'Tempo atual {data_am}')
print(data_am.tzinfo)
for time_zone in all_timezones:
    print(time_zone)