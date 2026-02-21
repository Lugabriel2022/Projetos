class Personagem():
	def __init__(self, nome):
		self.nome = nome
		self.modulos = {}

	def add_module(self, modulo):
		self.modulos[modulo.name] = modulo

	def get(self, name):
		return self.modulos.get(name)

	def has(self, name):
		return name in self.modulos

	def remove(self, name):
		if name in self.modulos:
			return self.modulos.pop(name)