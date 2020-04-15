import pygame
import block
import player


class Level:
	def __init__(self, fenster, levelnumber, player1, player2):
		self.fenster = fenster
		self.levelnumber = levelnumber
		self.leveldeath = False
		self.levelfeld_background = []
		self.levelfeld_foreground = []
		level = open("Level/Level"+ str(levelnumber) + ".txt").readlines()
		y = 0
		for line in level[1:]: #damit er die position der player nicht einliest
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
		standardposition = level[0].split(",")
		player1.standard_x = int(standardposition[0])
		player1.standard_y = int(standardposition[1])
		player2.standard_x = int(standardposition[2])
		player2.standard_y = int(standardposition[3])
	
	
	
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
				element.collziel(currentplayer, level)
				return False #soll er trotzdem weiterlaufen
		return False

		
	def die(self):
		self.leveldeath = True
	
