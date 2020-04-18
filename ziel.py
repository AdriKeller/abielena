import pygame
import block

"""
stellt eine Zieltür dar (Unterklasse von Block)
"""
class Ziel(block.Block):
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
	:return: Muss die Bewegung massiv gestoppt werden
	:rtype: bool
	"""
	def handleCollision(self, currentplayer):
		currentplayer.zielstate = self.wins(currentplayer) #wenn das eine True ist dann auch das andere
		return False

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
		super().__init__(fenster, x, y, "Bilder/p1ziel.png")
	
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
		super().__init__(fenster, x, y, "Bilder/p2ziel.png")
	
	"""
	Elemente der Klasse Ziel lassen den Spieler 2 gewinnen
	:param currentplayer: Spieler um den es geht
	:type currentplayer: player.Player
	:return: Spieler 2 is an seiner Tür
	:rtype: bool
	"""
	def wins(self, currentplayer):
		return currentplayer.name == "p2"
