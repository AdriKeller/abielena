import pygame
import player

"""
stellt einen einzelnen Block dar
"""
class Block(object):
	"""
	erstelle einen neuen Block
	:param fenster: gibt fenster-Surface weiter um darauf malen zu können
	:param x: x-Position des Blocks (zwischen 0 und 29)
	:param y: y-Position des Blocks (zwischen 0 und 19)
	:param bildsource: path zur Bilddatei des Blocks
	:type fenster: pygame.display
	:type x: int
	:type y: int
	:type bildsource: str
	"""
	def __init__(self, fenster, x, y, bildsource):
		self.fenster = fenster
		
		self.x = x
		self.y = y
		
		self.height = 30
		self.width = 30
		
		self.bild = pygame.image.load(bildsource)
	
	"""
	malt den jeweiligen Block in die Fenster-Surface durch ein blit
	"""
	def draw(self):
		self.fenster.blit(self.bild, (self.x * 30, self.y * 30))
	
	"""
	Testet die Kollision zwischen dem Block und dem jeweiligen Spieler
	:param currentplayer: Spieler um den es geht
	:param level: das aktuelle Level
	:type currentplayer: player.Player
	:type level: level.Level
	:return: Gab es eine Kollision zwischen dem Player und dem Block
	:rtype: bool
	"""
	def collision(self, currentplayer, level):
		return ((self.width * self.x < currentplayer.x + currentplayer.bew_x + currentplayer.width) and (currentplayer.x + currentplayer.bew_x < self.width * (self.x + 1)) and (self.height * self.y  < currentplayer.y + currentplayer.bew_y + currentplayer.height) and (currentplayer.y + currentplayer.bew_y < self.height * (self.y + 1)))
	
	"""
	
	"""
	def handleCollision(self, currentplayer):
		return True

"""
stellt einen Stein dar (Unterklasse von Block)
"""
class Stein(Block):
	"""
	erstellt einen neuen Stein und ruft dabei die init funktion von Block auf
	:param fenster: gibt fenster-Surface weiter um darauf malen zu können
	:param x: x-Position des Blocks (zwischen 0 und 29)
	:param y: y-Position des Blocks (zwischen 0 und 19)
	:type fenster: pygame.display
	:type x: int
	:type y: int
	"""
	def __init__(self, fenster, x, y):
		super().__init__(fenster, x, y, "block.png")

"""
stellt eine Zieltür dar (Unterklasse von Block)
"""
class Ziel(Block):
	"""
	erstellt eine neuen Zieltür und ruft dabei die init funktion von Block auf
	:param fenster: gibt fenster-Surface weiter um darauf malen zu können
	:param x: x-Position des Blocks (zwischen 0 und 29)
	:param y: y-Position des Blocks (zwischen 0 und 19)
	:param bildsource: path zur Bilddatei des Blocks
	:type fenster: pygame.display
	:type x: int
	:type y: int
	:type bildsource: str
	"""
	def __init__(self, fenster, x, y, bildsource):
		super().__init__(fenster, x, y, bildsource)
		
		self.height = 60
		self.width = 30
	
	"""
	Legt fest ob der Spieler in seiner Zieltür ist
	:param currentplayer: Spieler um den es geht
	:type currentplayer: player.Player
	"""
	def handleCollision(self, currentplayer):
		currentplayer.zielstate = self.wins(currentplayer)

	"""
	Elemente der Klasse Ziel lassen einen Spieler grundsätzlich nicht gewinnen
	:param currentplayer: Spieler um den es geht
	:type currentplayer: player.Player
	:return: Spieler ist an seiner Tür
	:rtype: bool
	"""
	def wins(self, currentplayer):
		return False

"""
stellt die Zieltür für den ersten Player dar(rosa)
"""
class P1ziel(Ziel):
	"""
	erstellt die rosa Zieltür und ruft dabei die init funktion von Zieltür auf: setzt den Path für die Bilddatei
	:param fenster: gibt fenster-Surface weiter um darauf malen zu können
	:param x: x-Position des Blocks (zwischen 0 und 29)
	:param y: y-Position des Blocks (zwischen 0 und 19)
	:type fenster: pygame.display
	:type x: int
	:type y: int
	"""
	def __init__(self, fenster, x, y):
		super().__init__(fenster, x, y, "p1ziel.png")
	
	"""
	Elemente der Klasse Ziel lassen den Spieler 1 gewinnen
	:param currentplayer: Spieler um den es geht
	:type currentplayer: player.Player
	:return: Spieler 1 is an seiner Tür
	:rtype: bool
	"""
	def wins(self, currentplayer):
		return currentplayer.name == "p1"

"""
stellt die Zieltür für den zewiten Player dar (schwarz)
"""
class P2ziel(Ziel):
	"""
	erstellt die schwarze Zieltür und ruft dabei die init funktion von Zieltür auf: setzt den Path für die Bilddatei
	:param fenster: gibt fenster-Surface weiter um darauf malen zu können
	:param x: x-Position des Blocks (zwischen 0 und 29)
	:param y: y-Position des Blocks (zwischen 0 und 19)
	:type fenster: pygame.display
	:type x: int
	:type y: int
	"""
	def __init__(self, fenster, x, y):
		super().__init__(fenster, x, y, "p2ziel.png")
	
	"""
	Elemente der Klasse Ziel lassen den Spieler 2 gewinnen
	:param currentplayer: Spieler um den es geht
	:type currentplayer: player.Player
	:return: Spieler 2 is an seiner Tür
	:rtype: bool
	"""
	def wins(self, currentplayer):
		return currentplayer.name == "p2"

"""
stellt ein Becken dar
"""
class Becken(Block):
	"""
	erstellt ein neues Becken und ruft dabei die init funktion von Block aus
	:param fenster: gibt fenster-Surface weiter um darauf malen zu können
	:param x: x-Position des Blocks (zwischen 0 und 29)
	:param y: y-Position des Blocks (zwischen 0 und 19)
	:param bildsource: path zur Bilddatei des Blocks
	:type fenster: pygame.display
	:type x: int
	:type y: int
	:type bildsource: str
	"""
	def __init__(self, fenster, x, y, bildsource):
		super().__init__(fenster, x, y, bildsource)
	
	"""
	löst das Sterben aus
	:param currentplayer: Spieler um den es geht
	:type currentplayer: player.Player
	"""
	def handleCollision(self, currentplayer):

		if (self.height * (self.y + 2/3)  < currentplayer.y + currentplayer.bew_y + currentplayer.height):
			currentplayer.bew_y = currentplayer.bew_y / 3

			if currentplayer.bew_y > 0:

				if self.kills(currentplayer):
					currentplayer.die()
			
			return True
		
		else:
			return False
	
	"""
	Elemente dieser Klasse sind grundsätzlich nicht tötlich für die Spieler
	:param currentplayer: Spieler um den es geht
	:type currentplayer: player.Player
	:return: Becken für den jeweiligen Spieler tödlich
	:rtype: bool
	"""
	def kills(self, currentplayer):
		return False

"""
stellt ein Becken der Farbe des Spieler 1 dar (rosa)
"""
class P1becken(Becken):
	"""
	erstellt ein neues Becken der Farbe Spieler 1 und ruft dabei die init Funktion von Becken auf: setzt den path für die Bilddatei
	:param fenster: gibt fenster-Surface weiter um darauf malen zu können
	:param x: x-Position des Blocks (zwischen 0 und 29)
	:param y: y-Position des Blocks (zwischen 0 und 19)
	:type fenster: pygame.display
	:type x: int
	:type y: int
	"""
	def __init__(self, fenster, x, y):
		super().__init__(fenster, x, y, "p1becken.png")
	
	"""
	Elemente dieser Klasse töten den Spieler namens p2
	:param currentplayer: Spieler um den es geht
	:type currentplayer: player.Player
	:return: Becken für den jeweiligen Spieler tödlich
	:rtype: bool
	"""
	def kills(self, currentplayer):
		return currentplayer.name == "p2"

"""
stellt ein Becken der Farbe des Spieler 2 dar (schwarz)
"""
class P2becken(Becken):
	"""
	erstellt ein neues Becken der Farbe Spieler 2 und ruft dabei die init Funktion von Becken auf: setzt den path für die Bilddatei
	:param fenster: gibt fenster-Surface weiter um darauf malen zu können
	:param x: x-Position des Blocks (zwischen 0 und 29)
	:param y: y-Position des Blocks (zwischen 0 und 19)
	:type fenster: pygame.display
	:type x: int
	:type y: int
	"""
	def __init__(self, fenster, x, y):
		super().__init__(fenster, x, y, "p2becken.png")
	
	"""
	Elemente dieser Klasse töten den Spieler namens p1
	:param currentplayer: Spieler um den es geht
	:type currentplayer: player.Player
	:return: Becken für den jeweiligen Spieler tödlich
	:rtype: bool
	"""
	def kills(self, currentplayer):
		return currentplayer.name == "p1"

"""
stellt ein giftiges Becken dar (grün)
"""
class Bothbecken(Becken):
	"""
	erstellt ein neues Becken der Farbe giftig und ruft dabei die init Funktion von Becken auf: setzt den path für die Bilddatei
	:param fenster: gibt fenster-Surface weiter um darauf malen zu können
	:param x: x-Position des Blocks (zwischen 0 und 29)
	:param y: y-Position des Blocks (zwischen 0 und 19)
	:type fenster: pygame.display
	:type x: int
	:type y: int
	"""
	def __init__(self, fenster, x, y):
		super().__init__(fenster, x, y, "bothbecken.png")
	
	"""
	Elemente dieser Klasse sind immer tödlich
	:param currentplayer: Spieler um den es geht
	:type currentplayer: player.Player
	:return: Becken für den jeweiligen Spieler tödlich
	:rtype: bool
	"""
	def kills(self, currentplayer):
		return True
