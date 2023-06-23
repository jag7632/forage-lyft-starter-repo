from abc import ABC, abstractmethod

class Servivable(ABC):
    @abstractmethod
    def needs_service(self):
        pass