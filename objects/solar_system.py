from .cosmic_entity import CosmicEntity
from .star import Star

class SolarSystem(CosmicEntity):
    def __init__(self, name):
        super().__init__(name)
        self.generate_children()

    def generate_children(self):
        self.children.append(Star("Main Star"))
