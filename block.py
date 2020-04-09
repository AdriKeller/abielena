import pygame


class Block(object):
	height = 30
	width = 30

class Stein(Block):
	self.blockbild = pygame.image.load("block.png")
	__init__(self, fenster, x, y):
		self.fenster.blit(blockbild, (x, y)) = fenster.blit(blockbild, (x, y))
		self.x = x
		self.y = y

class Becken(Block):
	pass
	
class P1becken(Becken):
	pass
	
class P2becken(Becken):
	pass
	
class Bothbecken(Becken):
	pass

