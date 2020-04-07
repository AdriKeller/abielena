import pygame

class Player(object):
	height = 30
	width = 15
	
	y = 550
	x = 30
	
	springstate = False
	springzahl = 5
	
	schritt = 10
	
	def __init__(self, x, y):
		self.x = x
		self.y = y
	
	def bew(self, richtung): # 1 für rechts, -1 für links
		self.x = self.x + richtung * self.schritt
	
		
	

