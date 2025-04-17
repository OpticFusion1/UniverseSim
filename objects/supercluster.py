from .cosmic_entity import CosmicEntity
from .galaxy_cluster import GalaxyCluster

class Supercluster(CosmicEntity):
    def __init__(self, name):
        super().__init__(name)
        self.generate_children()

    def generate_children(self):
        self.children.append(GalaxyCluster("GalaxyCluster-1"))