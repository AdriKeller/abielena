import pygame

class Block(object):
	height = 30
	width = 30
	def __init__(self, fenster, x, y, bild_url):
		self.fenster = fenster
		self.x = x
		self.y = y
		self.bild = pygame.image.load(bild_url)
		self.draw()

	def draw(self):
		self.fenster.blit(self.bild, (self.width * self.x, self.height * self.y))

class Stein(Block):
	def __init__(self, fenster, x, y):
		super().__init__(fenster, x, y, "block.png")

class Becken(Block):
	pass
	
class P1becken(Becken):
	pass
	
class P2becken(Becken):
	pass
	
class Bothbecken(Becken):
	pass

