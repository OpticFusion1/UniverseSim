import random
from .cosmic_entity import CosmicEntity
from .entity.entity import Entity
from .entity.humanentity import HumanEntity

class Planet(CosmicEntity):
    def __init__(self, name: str):
        super().__init__(name)

        # TODO: Make the day system more complex
        self.world_time = 0
        self.is_day_time = True
        self.day_count = 0
        self.max_day_ticks = 24000

        self.entities = []
        self.generate_children()

    def generate_children(self):
        self.entities.append(HumanEntity("Human"))

    def update(self):
        super().update()
        self.update_day()
        for entity in self.entities:
            entity.update()

    def render(self, indent: int = 0):
        super().render(indent)
        self.render_day(indent)
        print(" " * (indent + 2) + "Entities on planet:")
        for entity in self.entities:
            entity.render(indent)

    def update_day(self):
        self.world_time += 1

        self.time_of_day = self.world_time % self.max_day_ticks
        self.is_day_time = self.time_of_day < self.max_day_ticks / 2
        if (self.time_of_day == 0):
            self.day_count += 1

    def render_day(self, indent: int = 0):
        time_of_day = self.world_time % self.max_day_ticks
        time = "Day" if self.is_day_time else "Night"
        print(" " * (indent + 1) + f" Time of Day: {time_of_day} Days Passed: {self.day_count}")