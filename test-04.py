from core.base import Base

class Test(Base):

	def initialize(self):
		print("Inicializando programa...")

	def update(self):
		pass

#Crear una instancia de esta clase y correr el programa
Test().run()