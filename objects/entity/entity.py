from abc import ABC, abstractmethod

class Entity(ABC):

    def __init__(self, name):
        self.name = name

    @abstractmethod
    def update(self):
        pass

    @abstractmethod
    def render(self, indent: int = 0):
        pass

    def get_name(self):
        return self.name