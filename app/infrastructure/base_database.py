from abc import ABC, abstractmethod
from contextlib import contextmanager

class BaseDatabase(ABC):
    
    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def disconnect(self):
        pass

    @contextmanager
    @abstractmethod
    def get_db(self):
        pass



