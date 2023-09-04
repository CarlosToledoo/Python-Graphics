import pygame
import sys
from core.input import Input

class Base(object):

	def __init__(self):
			
		#Inicializar todos los modulos de pygame
		pygame.init()
		#Tamaño de la ventana
		screenSize = (512,512)
		# indicar las opts de render
		displayFlags = pygame.DOUBLEBUF | pygame.OPENGL

		# initialize buffers to perform antialiasing 
		pygame.display.gl_set_attribute(pygame.GL_MULTISAMPLEBUFFERS, 1) 
		pygame.display.gl_set_attribute(pygame.GL_MULTISAMPLESAMPLES, 4)

		# use a core OpenGL profile for cross-platform compatibility
		
		pygame.display.gl_set_attribute( pygame.GL_CONTEXT_PROFILE_MASK, 
										 pygame.GL_CONTEXT_PROFILE_CORE)

		# crear y mostrar la ventana
		self.screen = pygame.display.set_mode( screenSize, displayFlags ) 

		#título de la ventana
		pygame.display.set_caption("Carlos Miguel Toledo Ortigoza 202059265")

		# Determinar si el main loop es activo
		self.running = True

		# manage time-related data y operaciones
		self.clock = pygame.time.Clock()

		# manage user input 
		self.input = Input()

	#Implementado por clase extendida
	def initialize(self):
		pass

	# implementacion por clase extendida
	def update(self):
		pass

	def run(self):
  
		## starup ##
		self.initialize()

		##main loop##
		while self.running:

			## input proceso ##
			self.input.update()

			if self.input.quit:
				self.running = False

			## actualizar ##
			self.update()

			## render ##

			# mostrar imagen en pantalla 
			pygame.display.flip()

			# pause si es necesario to achieve 60 FPS
			self.clock.tick(60)

		## apagar ##
		pygame.quit()
		sys.exit()