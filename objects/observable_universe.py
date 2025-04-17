from .cosmic_entity import CosmicEntity
from .supercluster import Supercluster

class ObservableUniverse(CosmicEntity):
    def __init__(self):
        super().__init__("Observable Universe")
        self.should_render = True
        self.generate_children()

    def generate_children(self):
    	# TODO: Implement the ability to randomly generate a name
        self.children.append(Supercluster("Supercluster-1"))

    def render(self, indent=0):
        if not self.should_render:
            return  # Skip rendering this observable universe
        super().render(indent)