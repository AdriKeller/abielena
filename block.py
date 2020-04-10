import pygame



class Block(object):
	height = 30
	width = 30
	
	def __init__(self, fenster, x, y, bildsource):
		self.fenster = fenster
		self.x = x
		self.y = y
		self.bild = pygame.image.load(bildsource)
		
	def draw(self):
		self.fenster.blit(self.bild, (self.x, self.y))
		
		
		
class Stein(Block):
	def __init__(self, fenster, x, y):
		super().__init__(fenster, x, y, "block.png")


class Becken(Block):
	def __init__(self, fenster, x, y, bildsource):
		super().__init__(fenster, x, y, bildsource)
		


class P1becken(Becken):
	def __init__(self, fenster, x, y):
		super().__init__(fenster, x, y, "p1becken.png")
		

class P2becken(Becken):
	def __init__(self, fenster, x, y):
		super().__init__(fenster, x, y, "p2becken.png")
		

class Bothbecken(Becken):
	def __init__(self, fenster, x, y):
		super().__init__(fenster, x, y, "bothbecken.png")

