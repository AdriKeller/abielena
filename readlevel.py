import pygame
import block

class Level:
	def __init__(self, levelnumber, fenster):
		self.levelnumber = levelnumber
		self.fenster = fenster
		self.feld = [] #hier einen 2d-array generieren mit Blöcken

		level = open("Level/Level"+ str(self.levelnumber) + ".txt")
		y = 0
		for line in level:
			x = 0
			for element in line:
				if element == "1":
					block.Stein(self.fenster, x, y)
				x += 1
			y += 1
		
		self.draw()

	def draw(self):
		level = open("Level/Level"+ str(self.levelnumber) + ".txt")
		y = 0
		for line in level:
			x = 0
			for element in line:
				if element == "1":
					block.Stein(self.fenster, x, y)
				x += 1
			y += 1
	#	for line in self.feld:
	#		for element in line:
	#			element.draw
