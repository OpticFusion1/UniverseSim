from .cosmic_entity import CosmicEntity
from .supercluster import Supercluster

class ObservableUniverse(CosmicEntity):
    def __init__(self):
        super().__init__("Observable Universe")
        self.should_render = True
        self.generate_children()

    def generate_children(self):
        self.children.append(Supercluster("Supercluster-1"))

    def render(self, indent=0):
        if not self.should_render:
            return
        super().render(indent)