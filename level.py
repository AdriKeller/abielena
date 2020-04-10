import pygame
import block


class Level:
	def __init__(self, fenster, levelnumber):
		self.fenster = fenster
		self.levelnumber = levelnumber
		self.levelfeld = [] #2 dimensionale Liste mit den Blöcken usw
		level = open("Level/Level"+ str(levelnumber) + ".txt")
		unterliste = [] #jede y-Zeile
		y = 0
		for line in level: 
			x = 0
			for element in line:
				if element == "1":
					unterliste = unterliste + [block.Stein(fenster, x, y)]
				elif element == "2":
					unterliste = unterliste + [block.P1becken(fenster, x, y)]
				elif element == "3":
					unterliste = unterliste + [block.P2becken(fenster, x, y)]
				elif element == "4":
					unterliste = unterliste + [block.Bothbecken(fenster, x, y)]
				else: 
					unterliste = unterliste + []
				x = x + 1
			self.levelfeld = self.levelfeld + [unterliste] #liste generieren
			unterliste = [] #innere Liste wieder auf null stellen weil man von neuem anfängt
			y = y + 1
	
	
	def draw(self):
		for line in self.levelfeld:
			for element in line:
				#if element != None:
				element.draw() #element gehört zu block, dieser hat funktion draw()

