import pygame

class Player(object):
	
	
	schritt = 10
	
	
	def __init__(self, x, y, width, height, springstate, springzahl):
		self.x = x
		self.y = y
		self.width = width
		self.height = height
		self.springstate = springstate
		self.springzahl = springzahl
		self.hitbox = (x, y, width, height)
	
	def bew(self, richtung): # 1 für rechts, -1 für links
		self.x = self.x + richtung * self.schritt
	
papa = pygame.image.load("barbapapa.png")
papa = pygame.transform.scale(papa, (40, 40))
mama = pygame.image.load("barbamama.gif")
mama = pygame.transform.scale(mama, (30, 50))
	

