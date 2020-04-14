import pygame
import block


class Level:
	def __init__(self, fenster, levelnumber):
		self.fenster = fenster
		self.levelnumber = levelnumber
		self.levelfeld_background = []
		self.levelfeld_foreground = []
		level = open("Level/Level"+ str(levelnumber) + ".txt")
		y = 0
		for line in level: 
			x = 0
			for element in line:
				if element != "\n": #textdoc ist nach jeder Zeile ein Zeilensprung der abgelesen wird
					if element == "1":
						self.levelfeld_foreground = self.levelfeld_foreground + [block.Stein(fenster, x, y)]
					elif element == "2":
						self.levelfeld_foreground = self.levelfeld_foreground + [block.P1becken(fenster, x, y)]
					elif element == "3":
						self.levelfeld_foreground = self.levelfeld_foreground + [block.P2becken(fenster, x, y)]
					elif element == "4":
						self.levelfeld_foreground = self.levelfeld_foreground + [block.Bothbecken(fenster, x, y)]
					elif element == "5":
						self.levelfeld_background = self.levelfeld_background + [block.P1ziel(fenster, x, y)]
					elif element == "6":
						self.levelfeld_background = self.levelfeld_background + [block.P2ziel(fenster, x, y)]
					x = x + 1
			y = y + 1
	
	
	def draw_foreground(self):
		for element in self.levelfeld_foreground:
			element.draw() #element gehört zu block, dieser hat funktion draw()
				
	def draw_background(self):
		for element in self.levelfeld_background:
			element.draw() #element gehört zu block, dieser hat funktion draw()

	def collision(self, currentplayer, level): #geht alle einzelnen Blöcke durch und ruft für jeden einzelnen die collision funktion von block auf
		for element in self.levelfeld_foreground:
			if element.collision(currentplayer, level): #gleiche wie == True
				return True
		for element in self.levelfeld_background:
			if element.collision(currentplayer, level): #wenn es eine collision mit dem Ziel gibt
				return False #soll er trotzdem weiterlaufen
		return False

		
	def die(self):
		print("du bist gestorben")
	
	def win(self):
		print("du hast gewonnen")
