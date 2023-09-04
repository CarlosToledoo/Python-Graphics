import pygame

class Input(object):

	def __init__(self):
		
		#has the user quitar la app?
		self.quit = False

		#lists to store key states
		# dowm, up: discrete events, las for one iteration
		# pressed: continuos event, between down and up events
		self.keyDownList    = []
		self.keyPressedList = []
		self.keyUpList      = []

	def update(self):
		#iterate over all user inputs events(teclado/raton)
		# that have occured since last time events checked

		# reset discrete key states
		self.keyDownList = []
		self.keyUpList   = []

		for event in pygame.event.get():
			#quit event occurs by clicking button to close window
			if event.type == pygame.QUIT:
				self.quit = True
			#cheak for keydown and keyup events
			# get name of key from event
			# and append to or remove from corresponding list
			if event.type == pygame.KEYDOWN:
				keyName = pygame.key.name( event.key )
				self.keyDownList.append ( keyName )	
				self.keyPressedList.append( keyName)
			if event.type == pygame.KEYUP:
				keyName = pygame.key.name( event.key )
				self.keyPressedList.remove ( keyName )
				self.keyUpList.append( keyName )

	# functions to query key states
	def isKeyDown(self, keyName):
		return keyName in self.keyDownList

	def isKeyPressed(self, keyName):
		return keyName in self.keyPressedList

	def isKeyUp(self, keyName):
		return keyName in self.keyUpList
