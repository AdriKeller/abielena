import pygame
import block

"""
stellt eine Zieltuer dar (Unterklasse von Block)
"""
class Ziel(block.Block):	
	"""
	Legt fest ob der Spieler in seiner Zieltuer ist
	:param currentplayer: Spieler um den es geht
	:type currentplayer: player.Player
	:return: Muss die Bewegung gestoppt werden
	:rtype: bool
	"""
	def handleCollision(self, currentplayer):
		#wenn das eine True ist dann auch das andere
		currentplayer.zielstate = self.wins(currentplayer)
		return False
	
	"""
	Elemente der Klasse Ziel lassen einen Spieler grundsaetzlich nicht gewinnen
	:param currentplayer: Spieler um den es geht
	:type currentplayer: player.Player
	:return: Spieler ist an seiner Tuer
	:rtype: bool
	"""
	def wins(self, currentplayer):
		return False
	
	"""
	malt den jeweiligen Block in die Fenster-Surface durch ein blit
	"""
	def draw(self):
		self.fenster.blit(self.bild, (self.x * 30, (self.y - 1)* 30))

"""
stellt die Zieltuer fuer den ersten Player dar(rosa)
"""
class P1ziel(Ziel):
	"""
	erstellt die rosa Zieltuer und ruft dabei die init funktion von Zieltuer auf: setzt den Path fuer die Bilddatei
	:param fenster: gibt fenster-Surface weiter um darauf malen zu koennen
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
	:return: Spieler 1 is an seiner Tuer
	:rtype: bool
	"""
	def wins(self, currentplayer):
		return currentplayer.name == "p1"

"""
stellt die Zieltuer fuer den zewiten Player dar (schwarz)
"""
class P2ziel(Ziel):
	"""
	erstellt die schwarze Zieltuer und ruft dabei die init funktion von Zieltuer auf: setzt den Path fuer die Bilddatei
	:param fenster: gibt fenster-Surface weiter um darauf malen zu koennen
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
	:return: Spieler 2 is an seiner Tuer
	:rtype: bool
	"""
	def wins(self, currentplayer):
		return currentplayer.name == "p2"
