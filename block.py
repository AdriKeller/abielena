import pygame


class Block(object):
	height = 30
	width = 30

class Stein(Block):
	block1 = pygame.image.load("block.png")
	__init__(self, fenster, x, y):
		fenster.blit(block1, (200, 200))

class Becken(Block):
	pass
	
class P1becken(Becken):
	pass
	
class P2becken(Becken):
	pass
	
class Bothbecken(Becken):
	pass

