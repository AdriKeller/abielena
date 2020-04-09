import pygame


class Block(object):
	height = 30
	width = 30

class Stein(Block):
	blockbild = pygame.image.load("block.png")
	def __init__(self, fenster, x, y):
		print("Hallo"
		self.fenster = fenster
		self.x = x
		self.y = y
		self.fenster.blit(self.blockbild, (self.x, self.y))


class Becken(Block):
	pass
	
class P1becken(Becken):
	pass
	
class P2becken(Becken):
	pass
	
class Bothbecken(Becken):
	pass

