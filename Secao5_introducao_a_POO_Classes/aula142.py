# Classes abstratas - Abstract Base Class (abc)
# ABCs são usadas como contratos para a definição
# de novas classes. Elas podem forçar outras classes
# a criarem métodos concretos. Também podem ter
# métodos concretos por elas mesmas.
# @abstractmethods são métodos que não têm corpo.
# As regras para classes abstratas com métodos
# abstratos é que elas NÃO PODEM ser instânciadas
# diretamente.
# Métodos abstratos DEVEM ser implementados
# nas subclasses (@abstractmethod).
# Uma classe abstrata em Python tem sua metaclasse
# sendo ABCMeta.
# É possível criar @property @setter @classmethod
# @staticmethod e @method como abstratos, para isso
# use @abstractmethod como decorator mais interno.
from abc import ABC, abstractmethod

from pathlib import Path

LOG_FILE = Path(__file__).parent / 'log.txt'
class Log(ABC):
    @abstractmethod
    def _log(self, msg): ...

    def log_error(self, msg):
        return self._log(f'ERRO: {msg}')
    
    def log_success(self, msg):
        return self._log(f'Success: {msg}')
    
class LogFileMixin(Log):
    ...
    def _log(self, msg):
        print(__class__.__name__)
        msg_formatada = f'{msg} ({self.__class__.__name__})'
        # arquivo.write(msg_formatada)
        with open(LOG_FILE, 'a') as arquivo:
            arquivo.write(msg_formatada)
            arquivo.write('\r\n')
        
        
class LogPrintMixin(Log):
    ...
    def _log(self, msg):
        print(self.__class__.__name__)
        print(f'{msg} ({self.__class__.__name__})')
    
if __name__ == '__main__':
    t = Log( )
    t._log()
    