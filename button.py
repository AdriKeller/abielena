import pygame
import block


"""
stellt einen Button dar der einen Ghostblock aktiviert
"""	
class Button(block.Block):
	
	"""
	erstellt einen neuen Button und ruft dabei die init Funktion von Block auf
	:param fenster: gibt fenster-Surface weiter um darauf malen zu können
	:param x: x-Position des Blocks (zwischen 0 und 29)
	:param y: y-Position des Blocks (zwischen 0 und 19)
	:param bildsource: path zur Bilddatei des Blocks
	:type fenster: pygame.display
	:type x: int
	:type y: int
	:type bildsource: str
	"""
	def __init__(self, fenster, x, y):
		super().__init__(fenster, x, y, "Bilder/lilabutton_aktiv.png")
