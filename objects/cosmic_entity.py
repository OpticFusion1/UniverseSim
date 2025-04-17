from abc import ABC, abstractmethod

class CosmicEntity(ABC):
    def __init__(self, name: str):
        self.name = name
        self.children = []

    @abstractmethod
    def generate_children(self):
        pass

    def update(self):
        for child in self.children:
            child.update()

    def render(self, indent: int = 0):
        print(" " * indent + f"{self.name} ({len(self.children)} children)")
        for child in self.children:
            child.render(indent + 4)