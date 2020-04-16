import pygame
import block
import player

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
		level = open("Level/Level"+ str(levelnumber) + ".txt").readlines()
		
		y = 0
		#damit er die position der player nicht einliest
		for line in level[1:]:
			x = 0
			
			#erstellt zwei Listen mit den gesamten Elementen der Datei --> erstellt jedes Mal ein Objekt einer Klasse
			for element in line:

				if element != "\n":
					
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
			#element gehört zu block, dieser hat funktion draw()
			element.draw()

	"""
	geht alle einzelnen Blöcke durch und ruft für jeden einzelnen die collision funktion von block auf
	:param currentplayer: Spieler um den es geht
	:type currentplayer: player.Player
	:return: Gab es eine Kollision zwischen dem Player und einem Block
	:rtype: bool
	"""
	def collision(self, currentplayer):
		#geht die Liste mit den Steinen und Becken durch
		for element in self.levelfeld_foreground:
			
			#ruft die Collision-Methode aus block auf
			if element.collision(currentplayer, self):
				return True
		
		#geht die Liste mit den Zieltüren durch
		for element in self.levelfeld_background:
			
			#ruft die Collision-Methode aus block auf
			#wenn es eine collision mit dem Ziel gibt
			if element.collision(currentplayer, self):
				element.collziel(currentplayer)
				return False #er soll trotzdem weiterlaufen
		
		return False
	
	"""
	tot-variable wird  aktiv
	"""
	def die(self):
		self.leveldeath = True
