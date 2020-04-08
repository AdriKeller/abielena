import pygame

class Player(object):


	y = 550
	x = 30
	
	springstate = False
	springzahl = 5
	
	schritt = 10
	
	
	def __init__(self, x, y, width, height):
		self.x = x
		self.y = y
		self.width = width
		self.height = height
		self.hitbox = (self.x, self.y, self.width, self.height)
	
	def bew(self, richtung): # 1 für rechts, -1 für links
		self.x = self.x + richtung * self.schritt
	
papa = pygame.image.load("barbapapa.png")
papa = pygame.transform.scale(papa, (40, 40))
mama = pygame.image.load("barbamama.gif")
mama = pygame.transform.scale(mama, (30, 50))
	

