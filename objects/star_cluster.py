from .cosmic_entity import CosmicEntity
from .solar_system import SolarSystem

class StarCluster(CosmicEntity):
    def __init__(self, name):
        super().__init__(name)
        self.generate_children()

    def generate_children(self):
        self.children.append(SolarSystem("SolarSystem-1"))