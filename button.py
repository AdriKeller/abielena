import pygame
import block

"""
stellt einen Button dar der einen Ghostblock aktiviert
"""	
class Button(block.Block):
	"""
	erstellt einen neuen Button und ruft dabei die init Funktion von Block auf
	:param fenster: gibt fenster-Surface weiter um darauf malen zu koennen
	:param x: x-Position des Blocks (zwischen 0 und 29)
	:param y: y-Position des Blocks (zwischen 0 und 19)
	:param bildsource: path zur Bilddatei des Button
	:param aktivbild: path zur Bilddatei des aktiven (gedrueckten) Buttons
	:param game: aktuelles Spiel
	:type fenster: pygame.display
	:type x: int
	:type y: int
	:type bildsource: str
	:type aktivbild: str
	:type game: game.Game
	"""
	def __init__(self, fenster, x, y, bildsource, aktivbild, game):
		super().__init__(fenster, x, y, bildsource)
		self.game = game
		self.aktivbild = pygame.image.load(aktivbild)
		self.buttonstate = False
	
	"""
	Legt fest ob der Spieler den Knopf drueckt
	:param currentplayer: Spieler um den es geht
	:type currentplayer: player.Player
	:return: Muss die Bewegung gestoppt werden
	:rtype: bool
	"""
	def handleCollision(self, currentplayer):
		return False
	
	"""
	malt den Button in die Fenster-Surface durch ein blit, abhaengig davon ob er  gedrueckt ist oder nicht (anderes Bild)
	"""
	def draw(self):
		if self.buttonstate:
			self.fenster.blit(self.aktivbild, (self.x * 30, self.y * 30))
		
		else:
			self.fenster.blit(self.bild, (self.x * 30, self.y * 30))
		self.buttonstate = False

"""
stellt einen gelben Button dar, der den gelben Ghostblock steuert
"""
class Gelberbutton(Button):
	"""
	erstellt einen gelben durchlaessigen Stein und ruft dabei die init Funktion von Buttonghostblock auf
	:param fenster: gibt fenster-Surface weiter um darauf malen zu koennen
	:param x: x-Position des Buttons (zwischen 0 und 29)
	:param y: y-Position des Buttons (zwischen 0 und 19)
	:param game: aktuelles Spiel
	:type fenster: pygame.display
	:type x: int
	:type y: int
	:type game: game.Game
	"""
	def __init__(self, fenster, x, y, game):
		super().__init__(fenster, x, y, "Bilder/gelberbutton_inaktiv.png", "Bilder/gelberbutton_aktiv.png", game)
	
	"""
	Legt fest ob der Spieler den Knopf drueckt
	:param currentplayer: Spieler um den es geht
	:type currentplayer: player.Player
	:return: Muss die Bewegung gestoppt werden
	:rtype: bool
	"""
	def handleCollision(self, currentplayer):
		#fuer Ghostblocks relevant
		self.game.gelberbuttonstate = True
		#nur fuer Bild relevant
		self.buttonstate = True
		return False

"""
stellt einen roten Button dar, der den gelben Ghostblock steuert
"""	
class Roterbutton(Button):
	"""
	erstellt einen gelben durchlaessigen Stein und ruft dabei die init Funktion von Buttonghostblock auf
	:param fenster: gibt fenster-Surface weiter um darauf malen zu koennen
	:param x: x-Position des Buttons (zwischen 0 und 29)
	:param y: y-Position des Buttons (zwischen 0 und 19)
	:param game: aktuelles Spiel
	:type fenster: pygame.display
	:type x: int
	:type y: int
	:type game: game.Game
	"""
	def __init__(self, fenster, x, y, game):
		super().__init__(fenster, x, y, "Bilder/roterbutton_inaktiv.png", "Bilder/roterbutton_aktiv.png", game)
		
	"""
	Legt fest ob der Spieler den Knopf drueckt
	:param currentplayer: Spieler um den es geht
	:type currentplayer: player.Player
	:return: Muss die Bewegung gestoppt werden
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
	erstellt einen gelben durchlaessigen Stein und ruft dabei die init Funktion von Buttonghostblock auf
	:param fenster: gibt fenster-Surface weiter um darauf malen zu koennen
	:param x: x-Position des Buttons (zwischen 0 und 29)
	:param y: y-Position des Buttons (zwischen 0 und 19)
	:param game: aktuelles Spiel
	:type fenster: pygame.display
	:type x: int
	:type y: int
	:type game: game.Game
	"""
	def __init__(self, fenster, x, y, game):
		super().__init__(fenster, x, y, "Bilder/lilabutton_inaktiv.png", "Bilder/lilabutton_aktiv.png", game)
	
	"""
	Legt fest ob der Spieler den Knopf drueckt
	:param currentplayer: Spieler um den es geht
	:type currentplayer: player.Player
	:return: Muss die Bewegung gestoppt werden
	:rtype: bool
	"""
	def handleCollision(self, currentplayer):
		self.buttonstate = True
		self.game.lilabuttonstate = True
		return False
