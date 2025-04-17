from .cosmic_entity import CosmicEntity
from .galaxy import Galaxy

class GalaxyCluster(CosmicEntity):
    def __init__(self, name):
        super().__init__(name)
        self.generate_children()

    def generate_children(self):
        self.children.append(Galaxy("Galaxy-1"))