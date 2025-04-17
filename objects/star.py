from .cosmic_entity import CosmicEntity
from .planet import Planet

class Star(CosmicEntity):
    def __init__(self, name):
        super().__init__(name)
        self.generate_children()

    def generate_children(self):
        for i in range(3):
            self.children.append(Planet(f"Planet-{i + 1}"))
