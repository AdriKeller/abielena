import pygame
import block

"""
stellt einen durchgängigen Stein dar (Unterklasse von Block)
"""
class Ghostblock(block.Block):
	"""
	erstellt einen neuen durchgängigen Stein und ruft dabei die init funktion von Block auf
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
		

		
class Buttonghostblock(Ghostblock):
	
	"""
	erstellt einen neuen durchgängigen Stein und ruft dabei die init Funktion von Ghostbecken auf
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


class Playerghostblock(Ghostblock):
	
	"""
	erstellt einen neuen durchgängigen Stein pro Player und ruft dabei die init Funktion von Ghostbecken auf
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
