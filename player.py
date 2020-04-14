import pygame
import block
import level

class Player(object):
	
	
	def __init__(self, x, y, width, height, bildsource, fenster, name):
		self.x = x
		self.y = y
		self.width = width #von hitbox
		self.height = height #von hitbox
		self.bew_x = 0
		self.bew_y = 0
		self.schritt = 10
		self.darfspringen = True
		self.springzahl = 8
		self.fallzahl = 1
		self.darffallen = True
		self.fenster = fenster
		self.bild = pygame.image.load(bildsource)
		self.name = name
		self.zielstate = False
	
	def draw(self):
		self.fenster.blit(self.bild, (self.x, self.y))
	
	def bew(self, key_left, key_right, key_up, level):# 1 für rechts, -1 für links
		if key_left:
			self.bew_x = - self.schritt
		elif key_right:
			self.bew_x = self.schritt
			
		if self.darfspringen: #gleiches wie = True
			if key_up:
				self.darfspringen = False #ändern dass er nicht einmal durch den pygame loop durchgeht bevor er anfängt zu springen
		else:
			if self.springzahl > 0:
				self.bew_y = -(self.springzahl**2)
				self.springzahl = self.springzahl - 1 #counter springzahl
				self.darffallen = False
			else: #variablen resetten wenn der sprung fertig ist
				self.darfspringen = True
				self.springzahl = 8
				self.darffallen = True
		if not level.collision(self, level):#level ist in dem fall levelact
			self.y = self.y + self.bew_y #bewegung
			self.x = self.x + self.bew_x
		self.bew_x = 0
		self.bew_y = 0
	
	
	def grav(self, level): #gravitation: wenn er nirgendswo anstößt, fällt er weiter
		if self.darffallen:
			for x in range(4):
				self.bew_y = (self.fallzahl**2)/4 #man muss es teilen, damit bei der collision funktion nicht durchfällt
				if not level.collision(self, level):
					self.darfspringen = False
					self.y = self.y + self.bew_y
					self.darfspringen = True
				else:
					self.fallzahl = 1
					self.bew_y = 0
			if self.fallzahl < 6:
					self.fallzahl = self.fallzahl +1

	
			

