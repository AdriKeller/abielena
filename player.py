import pygame
import block
import level

class Player(object):
	
	
	schritt = 5
	
	
	def __init__(self, x, y, width, height, springstate, springzahl):
		self.x = x
		self.y = y
		self.width = width
		self.height = height
		self.springstate = springstate
		self.springzahl = springzahl
		#self.hitbox = (x, y, width, height)
	
	
	def bew(self, richtung, level):# 1 für rechts, -1 für links
		if not level.levelfeld[18][7].collision(self, richtung):
			self.x = self.x + richtung * self.schritt
		
	
	
	def jump(self, keypressed):
		if not self.springstate: #gleiches wie = False
			if keypressed :
				self.springstate = True
		else:
			if self.springzahl >= -5: #solange es 5 nicht erreicht
				if self.springzahl > 0:
					neg = 1
				else:
					neg = -1
				self.y = self.y - ((self.springzahl**2)*neg) #bewegung
				self.springzahl = self.springzahl - 2 #counter springzahl
			else: #variablen resetten wenn der sprung fertig ist
				self.springstate = False
				self.springzahl = 5
		

	
papa = pygame.image.load("barbapapa.png")
papa = pygame.transform.scale(papa, (40, 40))
mama = pygame.image.load("barbamama.gif")
mama = pygame.transform.scale(mama, (30, 50))
	

