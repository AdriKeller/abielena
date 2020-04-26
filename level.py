import pygame
import stein
import becken
import ziel
import ghostblock
import button

"""
stellt ein Level dar
"""
class Level:
	"""
	erstellt ein neues Level
	:param game: uebergibt die gesamte KLasse game
	:type game: game.Game
	"""
	def __init__(self, game):
		self.fenster = game.fenster
		
		self.leveldeath = False
		
		self.levelfeld_background = []
		self.levelfeld_foreground = []
		
		#readlines ist damit man nur eine Zeile ablesen kann mit bsp. [0]
		level = open("Level/Level" + str(game.levelnumber) + ".txt").readlines()
		
		self.bg = pygame.image.load((level[1])[:-1])
		
		y = 0
		#damit er die Position der Player  und den Hintergrund nicht einliest
		for line in level[2:]:
			x = 0
			
			#erstellt zwei Listen mit den gesamten Elementen der Datei --> erstellt jedes Mal ein Objekt einer Klasse
			for element in line:

				if element != "\n":
					
					if element == "1":
						self.levelfeld_foreground = self.levelfeld_foreground + [stein.Stein(self.fenster, x, y)]
					
					elif element == "2":
						self.levelfeld_foreground = self.levelfeld_foreground + [becken.P1becken(self.fenster, x, y)]
					
					elif element == "3":
						self.levelfeld_foreground = self.levelfeld_foreground + [becken.P2becken(self.fenster, x, y)]
					
					elif element == "4":
						self.levelfeld_foreground = self.levelfeld_foreground + [becken.Bothbecken(self.fenster, x, y)]
					
					elif element == "5":
						self.levelfeld_foreground = self.levelfeld_foreground + [becken.Nonebecken(self.fenster, x, y)]
					
					elif element == "6":
						self.levelfeld_background = self.levelfeld_background + [ziel.P1ziel(self.fenster, x, y)]
					
					elif element == "7":
						self.levelfeld_background = self.levelfeld_background + [ziel.P2ziel(self.fenster, x, y)]
					
					elif element == "l":
						self.levelfeld_foreground = self.levelfeld_foreground + [button.Lilabutton(self.fenster, x, y, game)]
					
					elif element == "L":
						self.levelfeld_background = self.levelfeld_background + [ghostblock.Lilaghostblock(self.fenster, x, y, game)]
					
					elif element == "r":
						self.levelfeld_foreground = self.levelfeld_foreground + [button.Roterbutton(self.fenster, x, y, game)]
					
					elif element == "R":
						self.levelfeld_background = self.levelfeld_background + [ghostblock.Roterghostblock(self.fenster, x, y, game)]
					
					elif element == "g":
						self.levelfeld_foreground = self.levelfeld_foreground + [button.Gelberbutton(self.fenster, x, y, game)]
					
					elif element == "G":
						self.levelfeld_background = self.levelfeld_background + [ghostblock.Gelberghostblock(self.fenster, x, y, game)]
					
					elif element == "P":
						self.levelfeld_background = self.levelfeld_background + [ghostblock.P1ghostblock(self.fenster, x, y)]
					
					elif element == "M":
						self.levelfeld_background = self.levelfeld_background + [ghostblock.P2ghostblock(self.fenster, x, y)]
					x = x + 1
			y = y + 1
		
		#erstellt eine Liste aus der ersten Zeile der Datei --> Elemente in Datei getrennt durch ein Komma
		standardposition = level[0].split(",")
		
		#stellt die Standardposition der Player fuer dieses Level ein
		game.p1.standard_x = int(standardposition[0])
		game.p1.standard_y = int(standardposition[1])
		game.p2.standard_x = int(standardposition[2])
		game.p2.standard_y = int(standardposition[3])
	
	"""
	Loop der durch die foreground-liste geht: Steine und Becken
	ruft fuer jedes einzelne Element die draw-methode auf aus block
	"""
	def draw_foreground(self):
		for element in self.levelfeld_foreground:
			element.draw()
	
	"""
	Loop der durch die foreground-liste geht: Zieltueren
	ruft fuer jedes einzelne Element die draw-methode auf aus block
	"""
	def draw_background(self):
		for element in self.levelfeld_background:
			element.draw()
	
	"""
	geht alle einzelnen Bloecke durch und ruft fuer jeden einzelnen die collision funktion von block auf
	:param currentplayer: Spieler um den es geht
	:type currentplayer: player.Player
	:return: Gab es eine Kollision zwischen dem Player und einem Block
	:rtype: bool
	"""
	def collision(self, currentplayer):
		currentplayer.zielstate = False
		collisionstate = False
		
		#addiert beide Listen
		for element in self.levelfeld_foreground + self.levelfeld_background:
			
			if element.collision(currentplayer):
				
				if element.handleCollision(currentplayer):
					collisionstate = True
		return collisionstate
