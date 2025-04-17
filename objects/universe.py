from .cosmic_entity import CosmicEntity
from .observable_universe import ObservableUniverse

class Universe(CosmicEntity):
    def __init__(self):
        super().__init__("Universe")
        self.generate_children()

    def generate_children(self):
        self.children.append(ObservableUniverse())