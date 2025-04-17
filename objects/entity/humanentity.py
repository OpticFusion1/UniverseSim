from .livingentity import LivingEntity

class HumanEntity(LivingEntity):

    def __init__(self, name):
        super().__init__(name, 100)

    def update(self):
        super().update()

    def render(self, indent: int = 0):
        super().render(indent)
        print(" " * (indent + 4) + f"Name: {self.get_name()} Health: {self.get_hp()}")