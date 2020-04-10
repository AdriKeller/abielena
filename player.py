import pygame
import block
import level

class Player(object):
	
	
	def __init__(self, x, y, width, height, bildsource, fenster):
		self.x = x
		self.y = y
		self.width = width #von hitbox
		self.height = height #von hitbox
		self.bew_x = 0
		self.bew_y = 0
		self.schritt = 5
		self.springstate = False
		self.springzahl = 5
		self.fenster = fenster
		self.bild = pygame.image.load(bildsource)
	
	def draw(self):
		self.fenster.blit(self.bild, (self.x, self.y))
	
	def bew(self, key_left, key_right, key_up, level):# 1 für rechts, -1 für links
		if key_left:
			self.bew_x = - self.schritt
		elif key_right:
			self.bew_x = self.schritt
			
		if not self.springstate: #gleiches wie = False
			if key_up :
				self.springstate = True #ändern dass er nicht einmal durch den pygame loop durchgeht bevor er anfängt zu springen
		else:
			if self.springzahl >= -5: #solange es -5 nicht erreicht
				self.springzahl = self.springzahl - 2 #counter springzahl
				if self.springzahl > 0:
					self.bew_y = - (self.springzahl**2)
				else:
					self.bew_y =  self.springzahl**2
			else: #variablen resetten wenn der sprung fertig ist
				self.springstate = False
				self.springzahl = 5
		if not level.collision(self):
			self.y = self.y + self.bew_y #bewegung
			self.x = self.x + self.bew_x



	
			

