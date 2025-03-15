# count é um iterador sem fim
from itertools import count
 
for _ in count(8,8):    
    if _ > 100:
        break
    print(_)