import pygame


class Block(object):
	height = 30
	width = 30

class Stein(Block):
	pass

class Becken(Block):
	pass
	
class P1becken(Becken):
	pass
	
class P2becken(Becken):
	pass
	
class Bothbecken(Becken):
	pass

block1 = pygame.image.load("block.png")
