import pygame
import block


class Level:
	def __init__(self, fenster, levelnumber):
		self.fenster = fenster
		self.levelnumber = levelnumber
		self.levelfeld = [] #2 dimensionale Liste mit den Blöcken usw
		level = open("Level/Level"+ str(levelnumber) + ".txt")
		unterliste = [None]*30 #jede y-Zeile
		y = 0
		for line in level: 
			x = 0
			for element in line:
				if element != "\n":
					if element == "1":
						unterliste[x] = [block.Stein(fenster, x, y)]
					elif element == "2":
						unterliste[x] = [block.P1becken(fenster, x, y)]
					elif element == "3":
						unterliste[x] = [block.P2becken(fenster, x, y)]
					elif element == "4":
						unterliste[x] = [block.Bothbecken(fenster, x, y)]
					x = x + 1
			self.levelfeld = self.levelfeld + [unterliste] #liste generieren
			unterliste = [None]*30 #innere Liste wieder auf null stellen weil man von neuem anfängt
			y = y + 1
	
	
	def draw(self):
		for line in self.levelfeld:
			for element in line:
				if element != None:
					print(element)
					element.draw() #element gehört zu block, dieser hat funktion draw()

