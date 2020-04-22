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
	:game: 
	"""
	def __init__(self, fenster, x, y, bildsource, aktivbild, game):
		super().__init__(fenster, x, y, bildsource)
		self.game = game
		self.inaktivbild = pygame.image.load(bildsource)
		self.aktivbild = pygame.image.load(aktivbild)


	"""
	Legt fest ob der Spieler den Knopf drückt
	:param currentplayer: Spieler um den es geht
	:type currentplayer: player.Player
	:return: Muss die Bewegung massiv gestoppt werden
	:rtype: bool
	"""
	def handleCollision(self, currentplayer):
		return False
		
	"""
	malt den Button in die Fenster-Surface durch ein blit, abhängig davon ob er  gedrückt ist oder nicht (anderes Bild)
	"""
	def draw(self):
		if self.buttonstate:
			self.fenster.blit(self.aktivbild, (self.x * 30, self.y * 30))
		else:
			self.fenster.blit(self.inaktivbild, (self.x * 30, self.y * 30))
		self.buttonstate = False

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
	def __init__(self, fenster, x, y, game):
		super().__init__(fenster, x, y, "Bilder/gelberbutton_inaktiv.png", "Bilder/gelberbutton_aktiv.png", game)
		self.buttonstate = False
		
	"""
	Legt fest ob der Spieler den Knopf drückt
	:param currentplayer: Spieler um den es geht
	:type currentplayer: player.Player
	:return: Muss die Bewegung massiv gestoppt werden
	:rtype: bool
	"""
	def handleCollision(self, currentplayer):
		self.game.gelberbuttonstate = True #für Ghostblocks relevant
		self.buttonstate = True #nur für Bild relevant
		return False


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
	def __init__(self, fenster, x, y, game):
		super().__init__(fenster, x, y, "Bilder/roterbutton_inaktiv.png", "Bilder/roterbutton_aktiv.png", game)
		self.buttonstate = False
		
	"""
	Legt fest ob der Spieler den Knopf drückt
	:param currentplayer: Spieler um den es geht
	:type currentplayer: player.Player
	:return: Muss die Bewegung massiv gestoppt werden
	:rtype: bool
	"""
	def handleCollision(self, currentplayer):
		self.game.roterbuttonstate = True
		self.buttonstate = True
		return False

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
	def __init__(self, fenster, x, y, game):
		super().__init__(fenster, x, y, "Bilder/lilabutton_inaktiv.png", "Bilder/lilabutton_aktiv.png", game)
		self.buttonstate = False
		
	"""
	Legt fest ob der Spieler den Knopf drückt
	:param currentplayer: Spieler um den es geht
	:type currentplayer: player.Player
	:return: Muss die Bewegung massiv gestoppt werden
	:rtype: bool
	"""
	def handleCollision(self, currentplayer):
		self.buttonstate = True
		self.game.lilabuttonstate = True
		return False
