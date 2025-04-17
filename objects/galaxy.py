from .cosmic_entity import CosmicEntity
from .star_cluster import StarCluster

class Galaxy(CosmicEntity):
    def __init__(self, name):
        super().__init__(name)
        self.generate_children()

    def generate_children(self):
        self.children.append(StarCluster("StarCluster-1"))