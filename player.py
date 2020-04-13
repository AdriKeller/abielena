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
		self.schritt = 5
		self.springstate = False
		self.springzahl = 8
		self.fallzahl = -2
		self.fenster = fenster
		self.bild = pygame.image.load(bildsource)
		self.name = name
	
	def draw(self):
		self.fenster.blit(self.bild, (self.x, self.y))
	
	def bew(self, key_left, key_right, key_up, level):# 1 für rechts, -1 für links
		if key_left:
			self.bew_x = - self.schritt
		elif key_right:
			self.bew_x = self.schritt
			
		if not self.springstate: #gleiches wie = False
			if key_up:
				self.springstate = True #ändern dass er nicht einmal durch den pygame loop durchgeht bevor er anfängt zu springen
		else:
			if self.springzahl > 0:
				self.bew_y = -(self.springzahl**2)
				self.springzahl = self.springzahl - 2 #counter springzahl
			else: #variablen resetten wenn der sprung fertig ist
				self.springstate = False
				self.springzahl = 8
		if not level.collision(self, level):
			self.y = self.y + self.bew_y #bewegung
			self.x = self.x + self.bew_x
		#if not self.springstate:
		#	self.grav(level)
		self.bew_x = 0
		self.bew_y = 0
	
	
	def grav(self, level): #gravitation: wenn er nirgendswo anstößt, fällt er weiter
		self.bew_y = self.fallzahl**2
		if not level.collision(self, level):
			self.springstate = True
			self.y = self.y + self.bew_y
			self.fallzahl = self.fallzahl -2
			self.springstate = False
		else:
			 self.fallzahl = -2
			 self.bew_y = 0


	
			

