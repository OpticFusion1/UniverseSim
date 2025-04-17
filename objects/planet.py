import random
from .cosmic_entity import CosmicEntity

class Planet(CosmicEntity):
    def __init__(self, name: str):
        super().__init__(name)
        self.entities = []
        self.generate_children()

    def generate_children(self):
        print("No children to generate")

    def update(self):
        super().update()
        for entity in self.entities:
            entity.update()

    def render(self, indent: int = 0):
        super().render(indent)
        print(" " * (indent + 2) + "Entities on planet:")
        for entity in self.entities:
            print(" " * (indent + 4) + str(entity))