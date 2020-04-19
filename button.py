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
	:param bildsource: path zur Bilddatei des Button
	:param aktivbild: path zur Bilddatei des aktiven (gedrückten) Buttons
	:type fenster: pygame.display
	:type x: int
	:type y: int
	:type bildsource: str
	:type aktivbild: str
	"""
	def __init__(self, fenster, x, y, bildsource, aktivbild):
		super().__init__(fenster, x, y, bildsource)


	"""
	Legt fest ob der Spieler den Knopf drückt
	:param currentplayer: Spieler um den es geht
	:type currentplayer: player.Player
	:return: Muss die Bewegung massiv gestoppt werden
	:rtype: bool
	"""
	def handleCollision(self, currentplayer):
		se
		
		return False
		
	
	def draw(self):
		if True:
			self.fenster.blit(self.bild, (self.x * 30, self.y * 30))

"""
stellt einen gelben Button dar, der den gelben Ghostblock steuert
"""	
class Gelberbutton(Button):
	
	"""
	erstellt einen gelben durchlässigen Stein und ruft dabei die init Funktion von Buttonghostblock auf
	:param fenster: gibt fenster-Surface weiter um darauf malen zu können
	:param x: x-Position des Buttons (zwischen 0 und 29)
	:param y: y-Position des Buttons (zwischen 0 und 19)
	:type fenster: pygame.display
	:type x: int
	:type y: int
	"""
	def __init__(self, fenster, x, y):
		super().__init__(fenster, x, y, "Bilder/gelberbutton_inaktiv.png", "Bilder/gelberbutton_aktiv.png")


"""
stellt einen roten Button dar, der den gelben Ghostblock steuert
"""	
class Roterbutton(Button):
	
	"""
	erstellt einen gelben durchlässigen Stein und ruft dabei die init Funktion von Buttonghostblock auf
	:param fenster: gibt fenster-Surface weiter um darauf malen zu können
	:param x: x-Position des Buttons (zwischen 0 und 29)
	:param y: y-Position des Buttons (zwischen 0 und 19)
	:type fenster: pygame.display
	:type x: int
	:type y: int
	"""
	def __init__(self, fenster, x, y):
		super().__init__(fenster, x, y, "Bilder/roterbutton_inaktiv.png", "Bilder/roterbutton_aktiv.png")

"""
stellt einen lilanen Button dar, der den gelben Ghostblock steuert
"""	
class Lilabutton(Button):
	
	"""
	erstellt einen gelben durchlässigen Stein und ruft dabei die init Funktion von Buttonghostblock auf
	:param fenster: gibt fenster-Surface weiter um darauf malen zu können
	:param x: x-Position des Buttons (zwischen 0 und 29)
	:param y: y-Position des Buttons (zwischen 0 und 19)
	:type fenster: pygame.display
	:type x: int
	:type y: int
	"""
	def __init__(self, fenster, x, y):
		super().__init__(fenster, x, y, "Bilder/lilabutton_inaktiv.png", "Bilder/lilabutton_aktiv.png", )
