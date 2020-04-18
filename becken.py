import pygame
import block

"""
stellt ein Becken dar
"""
class Becken(block.Block):
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
		#verlangsamt den Player
		#currentplayer.bew_x = currentplayer.bew_x / 2
		
		#ob er den Boden berührt
		if (self.height * (self.y + 2/3)  < currentplayer.y + currentplayer.bew_y + currentplayer.height): 
			#er stirbt erst wenn er den Boden berührt und von oben kommt
			if (currentplayer.bew_y > 0) and self.kills(currentplayer):
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
		super().__init__(fenster, x, y, "Bilder/p1becken.png")
	
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
		super().__init__(fenster, x, y, "Bilder/p2becken.png")
	
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
stellt ein harmloses Becken dar (blau)
"""

class Nonebecken(Becken):
	"""
	erstellt ein neues Becken der Farbe harmlos und ruft dabei die init Funktion von Becken auf: setzt den path für die Bilddatei
	:param fenster: gibt fenster-Surface weiter um darauf malen zu können
	:param x: x-Position des Blocks (zwischen 0 und 29)
	:param y: y-Position des Blocks (zwischen 0 und 19)
	:type fenster: pygame.display
	:type x: int
	:type y: int
	"""
	def __init__(self, fenster, x, y):
		super().__init__(fenster, x, y, "Bilder/nonebecken.png")
	
	"""
	Elemente dieser Klasse sind nie tödlich
	:param currentplayer: Spieler um den es geht
	:type currentplayer: player.Player
	:return: Becken für den jeweiligen Spieler tödlich
	:rtype: bool
	"""
	def kills(self, currentplayer):
		return False


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
		super().__init__(fenster, x, y, "Bilder/bothbecken.png")
	
	"""
	Elemente dieser Klasse sind immer tödlich
	:param currentplayer: Spieler um den es geht
	:type currentplayer: player.Player
	:return: Becken für den jeweiligen Spieler tödlich
	:rtype: bool
	"""
	def kills(self, currentplayer):
		return True
