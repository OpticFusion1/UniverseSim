from .entity import Entity

class LivingEntity(Entity):

	def __init__(self, name, max_hp):
		super().__init__(name)
		self.max_hp = max_hp
		self.current_hp = max_hp

	def get_hp(self):
		return self.current_hp

	def is_alive(self):
		return self.current_hp > 0

	def kill(self):
		self.current_hp = 0

	def heal(self, amount):
		self.current_hp = self.current_hp + amount