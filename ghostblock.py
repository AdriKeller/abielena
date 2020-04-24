import pygame
import block

"""
stellt einen durchlaessigen Stein dar (Unterklasse von Block)
"""
class Ghostblock(block.Block):
	"""
	erstellt einen neuen durchlaessigen Stein und ruft dabei die init funktion von Block auf
	:param fenster: gibt fenster-Surface weiter um darauf malen zu koennen
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
	gibt an ob der Stein die Bewegung des Players stoppen muss
	:param currentplayer: Spieler um den es geht
	:type currentplayer: player.Player
	:return: Ob der Stein die Bewegung des Players stoppen soll
	:rtype: bool
	"""
	def handleCollision(self, currentplayer):
		return not self.durchlassen(currentplayer)
	
	"""
	gibt Durchlaessigkeit des Steins an
	:param currentplayer: Spieler um den es geht
	:type currentplayer: player.Player
	:return: ob Stein durchlaessig ist
	:rtype: bool
	"""
	def durchlassen(self, currentplayer):
		return False

"""
stellt einen durchlaessigen Stein dar, der duch Button gesteuert wird (Unterklasse von Ghostblock)
"""
class Buttonghostblock(Ghostblock):
	"""
	erstellt einen neuen durchlaessigen Stein und ruft dabei die init Funktion von Ghostblock auf
	:param fenster: gibt fenster-Surface weiter um darauf malen zu koennen
	:param x: x-Position des Blocks (zwischen 0 und 29)
	:param y: y-Position des Blocks (zwischen 0 und 19)
	:param bildsource: path zur Bilddatei des Blocks
	:param ghostbild: path zur durchsichtigen Bilddatei des Blocks
	:param game: aktuelles Spiel
	:type fenster: pygame.display
	:type x: int
	:type y: int
	:type bildsource: str
	:type ghostbild: str
	:type game: game.Game
	"""
	def __init__(self, fenster, x, y, bildsource, ghostbild, game):
		super().__init__(fenster, x, y, bildsource)
		self.game = game
		self.ghostbild = pygame.image.load(ghostbild)
	
	"""
	gibt an ob der Stein die Bewegung des Players stoppen muss
	:param currentplayer: Spieler um den es geht
	:type currentplayer: player.Player
	:return: Ob der Stein die Bewegung des Players stoppen soll
	:rtype: bool
	"""
	def handleCollision(self, currentplayer):
		#nach dem or: damit Player nicht im Stein stecken bleibt
		return not (self.durchlassen(currentplayer) or ((self.width * self.x < currentplayer.x + currentplayer.width) and (currentplayer.x < self.width * (self.x + 1)) and (self.height * self.y  < currentplayer.y + currentplayer.height) and (currentplayer.y < self.height * (self.y + 1))))

"""
stellt einen gelben durchlaessigen Stein dar, der durch Button gesteuert wird (Unterklasse von Buttonghostblock)
"""
class Gelberghostblock(Buttonghostblock):
	"""
	erstellt einen gelben durchlaessigen Stein und ruft dabei die init Funktion von Buttonghostblock auf
	:param fenster: gibt fenster-Surface weiter um darauf malen zu koennen
	:param x: x-Position des Blocks (zwischen 0 und 29)
	:param y: y-Position des Blocks (zwischen 0 und 19)
	:param game: aktuelles Spiel
	:type fenster: pygame.display
	:type x: int
	:type y: int
	:type game: game.Game
	"""
	def __init__(self, fenster, x, y, game):
		super().__init__(fenster, x, y, "Bilder/gelberblock.png", "Bilder/gelberblock_ghost.png", game)
	
	"""
	malt den Block in die Fenster-Surface durch ein blit, abhaengig davon ob der Button gedrueckt ist oder nicht (anderes Bild)
	"""
	def draw(self):
		if self.game.gelberbuttonstate:
			self.fenster.blit(self.ghostbild, (self.x * 30, self.y * 30))
		
		else:
			self.fenster.blit(self.bild, (self.x * 30, self.y * 30))
	
	"""
	gibt Durchlaessigkeit des Steins an
	:param currentplayer: Spieler um den es geht
	:type currentplayer: player.Player
	:return: ob Stein durchlaessig ist --> von Buttonstate abhaengig
	:rtype: bool
	"""
	def durchlassen(self, currentplayer):
		return self.game.gelberbuttonstate

"""
stellt einen lilanen durchlaessigen Stein dar, der durch Button gesteuert wird (Unterklasse von Buttonghostblock)
"""
class Lilaghostblock(Buttonghostblock):
	"""
	erstellt einen lilanen durchlaessigen Stein und ruft dabei die init Funktion von Buttonghostblock auf
	:param fenster: gibt fenster-Surface weiter um darauf malen zu koennen
	:param x: x-Position des Blocks (zwischen 0 und 29)
	:param y: y-Position des Blocks (zwischen 0 und 19)
	:param game: aktuelles Spiel
	:type fenster: pygame.display
	:type x: int
	:type y: int
	:type game: game.Game
	"""
	def __init__(self, fenster, x, y, game):
		super().__init__(fenster, x, y, "Bilder/lilablock.png", "Bilder/lilablock_ghost.png", game)
	
	"""
	malt den Block in die Fenster-Surface durch ein blit, abhaengig davon ob der Button gedrueckt ist oder nicht (anderes Bild)
	"""
	def draw(self):
		if self.game.lilabuttonstate:
			self.fenster.blit(self.ghostbild, (self.x * 30, self.y * 30))
		
		else:
			self.fenster.blit(self.bild, (self.x * 30, self.y * 30))
	
	"""
	gibt Durchlaessigkeit des Steins an
	:param currentplayer: Spieler um den es geht
	:type currentplayer: player.Player
	:return: ob Stein durchlaessig ist --> von Buttonstate abhaengig
	:rtype: bool
	"""
	def durchlassen(self, currentplayer):
		return self.game.lilabuttonstate

"""
stellt einen roten durchlaessigen Stein dar, der durch Button gesteuert wird (Unterklasse von Buttonghostblock)
"""
class Roterghostblock(Buttonghostblock):
	"""
	erstellt einen roten durchlaessigen Stein und ruft dabei die init Funktion von Buttonghostblock auf
	:param fenster: gibt fenster-Surface weiter um darauf malen zu koennen
	:param x: x-Position des Blocks (zwischen 0 und 29)
	:param y: y-Position des Blocks (zwischen 0 und 19)
	:param game: aktuelles Spiel
	:type fenster: pygame.display
	:type x: int
	:type y: int
	:type game: game.Game
	"""
	def __init__(self, fenster, x, y, game):
		super().__init__(fenster, x, y, "Bilder/roterblock.png", "Bilder/roterblock_ghost.png", game)
	
	"""
	malt den Block in die Fenster-Surface durch ein blit, abhaengig davon ob der Button gedrueckt ist oder nicht (anderes Bild)
	"""
	def draw(self):
		if self.game.roterbuttonstate:
			self.fenster.blit(self.bild, (self.x * 30, self.y * 30))
		
		else:
			self.fenster.blit(self.ghostbild, (self.x * 30, self.y * 30))
	
	"""
	gibt Durchlaessigkeit des Steins an
	:param currentplayer: Spieler um den es geht
	:type currentplayer: player.Player
	:return: ob Stein durchlaessig ist --> von Buttonstate abhaengig
	:rtype: bool
	"""
	def durchlassen(self, currentplayer):
		#andersrum als bei gelb und lila: laesst nicht durch wenn gedrueckt
		return not self.game.roterbuttonstate

"""
stellt einen rosanen fuer P1 durchlaessigen Stein dar (Unterklasse von Ghostblock)
"""
class P1ghostblock(Ghostblock):
	"""
	erstellt einen rosanen durchlaessigen Stein und ruft dabei die init Funktion von Playerghostblock auf
	:param fenster: gibt fenster-Surface weiter um darauf malen zu koennen
	:param x: x-Position des Blocks (zwischen 0 und 29)
	:param y: y-Position des Blocks (zwischen 0 und 19)
	:type fenster: pygame.display
	:type x: int
	:type y: int
	"""
	def __init__(self, fenster, x, y):
		super().__init__(fenster, x, y, "Bilder/rosablock.png")
	
	"""
	gibt Durchlaessigkeit des Steins an
	:param currentplayer: Spieler um den es geht
	:type currentplayer: player.Player
	:return: ob Stein durchlaessig ist --> vom jeweiligen Player abhaengig
	:rtype: bool
	"""
	def durchlassen(self, currentplayer):
		return currentplayer.name == "p1"

"""
stellt einen schwarzen fuer P2 durchlaessigen Stein dar (Unterklasse von Ghostblock)
"""
class P2ghostblock(Ghostblock):
	"""
	erstellt einen schwarzen durchlaessigen Stein und ruft dabei die init Funktion von Playerghostblock auf
	:param fenster: gibt fenster-Surface weiter um darauf malen zu koennen
	:param x: x-Position des Blocks (zwischen 0 und 29)
	:param y: y-Position des Blocks (zwischen 0 und 19)
	:type fenster: pygame.display
	:type x: int
	:type y: int
	"""
	def __init__(self, fenster, x, y):
		super().__init__(fenster, x, y, "Bilder/schwarzerblock.png")
	
	"""
	gibt Durchlaessigkeit des Steins an
	:param currentplayer: Spieler um den es geht
	:type currentplayer: player.Player
	:return: ob Stein durchlaessig ist --> vom jeweiligen Player abhaengig
	:rtype: bool
	"""
	def durchlassen(self, currentplayer):
		return currentplayer.name == "p2"
