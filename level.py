import pygame
import block
import player
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
	:param fenster: gibt das Fenster von main weiter
	:param levelnumber: zahl vom level um die jeweilige Datei zu öffnen
	:param player1: übergibt alles von p1
	:param player2: übergibt alles von p2
	:type fenster: pygame.display
	:type levelnumber: int
	:type player1: player.Player
	:type player1: player.Player
	"""
	def __init__(self, fenster, levelnumber, player1, player2):
		self.fenster = fenster
		
		self.levelnumber = levelnumber
		
		self.leveldeath = False
		
		self.levelfeld_background = []
		self.levelfeld_foreground = []
		
		#readlines ist damit man nur eine Zeile ablesen kann mit bsp. [0]
		level = open("Level/Level" + str(levelnumber) + ".txt").readlines()
		
		y = 0
		#damit er die position der player nicht einliest
		for line in level[1:]:
			x = 0
			
			#erstellt zwei Listen mit den gesamten Elementen der Datei --> erstellt jedes Mal ein Objekt einer Klasse
			for element in line:

				if element != "\n":
					
					if element == "1":
						self.levelfeld_foreground = self.levelfeld_foreground + [stein.Stein(fenster, x, y)]
					
					elif element == "2":
						self.levelfeld_foreground = self.levelfeld_foreground + [becken.P1becken(fenster, x, y)]
					
					elif element == "3":
						self.levelfeld_foreground = self.levelfeld_foreground + [becken.P2becken(fenster, x, y)]
					
					elif element == "4":
						self.levelfeld_foreground = self.levelfeld_foreground + [becken.Bothbecken(fenster, x, y)]
					
					elif element == "5":
						self.levelfeld_foreground = self.levelfeld_foreground + [becken.Nonebecken(fenster, x, y)]
					
					elif element == "6":
						self.levelfeld_background = self.levelfeld_background + [ziel.P1ziel(fenster, x, y)]
					
					elif element == "7":
						self.levelfeld_background = self.levelfeld_background + [ziel.P2ziel(fenster, x, y)]
						
					elif element == "l":
						self.levelfeld_background = self.levelfeld_background + [button.Lilabutton(fenster, x, y)]
					
					elif element == "L":
						self.levelfeld_background = self.levelfeld_background + [ghostblock.Lilaghostblock(fenster, x, y)]
					
					elif element == "r":
						self.levelfeld_background = self.levelfeld_background + [button.Button(fenster, x, y)]
					
					elif element == "R":
						self.levelfeld_background = self.levelfeld_background + [ghostblock.Roterghostblock(fenster, x, y)]
					
					elif element == "g":
						self.levelfeld_background = self.levelfeld_background + [button.Gelberbutton(fenster, x, y)]
					
					elif element == "G":
						self.levelfeld_background = self.levelfeld_background + [ghostblock.Gelberghostblock(fenster, x, y)]
					
					elif element == "P":
						self.levelfeld_background = self.levelfeld_background + [ghostblock.P1ghostblock(fenster, x, y)]
					
					elif element == "M":
						self.levelfeld_background = self.levelfeld_background + [ghostblock.P2ghostblock(fenster, x, y)]
					
					x = x + 1
			
			y = y + 1
		
		#erstellt eine Liste aus der ersten Zeile der Datei --> 2 Elemente getrennt durch ein Komma
		standardposition = level[0].split(",")
		
		#stellt die Standardposition der Player für dieses Level ein
		player1.standard_x = int(standardposition[0])
		player1.standard_y = int(standardposition[1])
		
		player2.standard_x = int(standardposition[2])
		player2.standard_y = int(standardposition[3])
	
	"""
	Loop der durch die foreground-liste geht: Steine und Becken
	ruft für jedes einzelne Element die draw-methode auf aus block
	"""
	def draw_foreground(self):
		for element in self.levelfeld_foreground:
			element.draw()
	
	"""
	Loop der durch die foreground-liste geht: Zieltüren
	ruft für jedes einzelne Element die draw-methode auf aus block
	"""
	def draw_background(self):
		for element in self.levelfeld_background:
			element.draw()

	"""
	geht alle einzelnen Blöcke durch und ruft für jeden einzelnen die collision funktion von block auf
	:param currentplayer: Spieler um den es geht
	:type currentplayer: player.Player
	:return: Gab es eine Kollision zwischen dem Player und einem Block
	:rtype: bool
	"""
	def collision(self, currentplayer):
		collisionstate = False
		
		for element in self.levelfeld_foreground + self.levelfeld_background: #addiert beide Listen
			
			if element.collision(currentplayer):
				
				if element.handleCollision(currentplayer):
					collisionstate = True
		
		return collisionstate
