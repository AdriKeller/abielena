import pygame
import block

"""
stellt einen durchlässigen Stein dar (Unterklasse von Block)
"""
class Ghostblock(block.Block):
	"""
	erstellt einen neuen durchlässigen Stein und ruft dabei die init funktion von Block auf
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
	gibt an ob der Stein die Bewegung des Players stoppen muss
	:param currentplayer: Spieler um den es geht
	:type currentplayer: player.Player
	:return: Ob der Stein die Bewegung des Players stoppen soll
	:rtype: bool
	"""
	def handleCollision(self, currentplayer):
		return not self.durchlassen(currentplayer)
	
	"""
	gibt Durchlässigkeit des Steins an
	:param currentplayer: Spieler um den es geht
	:type currentplayer: player.Player
	:return: ob Stein durchlässig ist
	:rtype: bool
	"""
	def durchlassen(self, currentplayer):
		return False

"""
stellt einen durchlässigen Stein dar, der duch Button gesteuert wird (Unterklasse von Ghostblock)
"""
class Buttonghostblock(Ghostblock):
	"""
	erstellt einen neuen durchlässigen Stein und ruft dabei die init Funktion von Ghostblock auf
	:param fenster: gibt fenster-Surface weiter um darauf malen zu können
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
stellt einen gelben durchlässigen Stein dar, der durch Button gesteuert wird (Unterklasse von Buttonghostblock)
"""
class Gelberghostblock(Buttonghostblock):
	"""
	erstellt einen gelben durchlässigen Stein und ruft dabei die init Funktion von Buttonghostblock auf
	:param fenster: gibt fenster-Surface weiter um darauf malen zu können
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
	malt den Block in die Fenster-Surface durch ein blit, abhängig davon ob der Button gedrückt ist oder nicht (anderes Bild)
	"""
	def draw(self):
		if self.game.gelberbuttonstate:
			self.fenster.blit(self.ghostbild, (self.x * 30, self.y * 30))
		
		else:
			self.fenster.blit(self.bild, (self.x * 30, self.y * 30))
	
	"""
	gibt Durchlässigkeit des Steins an
	:param currentplayer: Spieler um den es geht
	:type currentplayer: player.Player
	:return: ob Stein durchlässig ist --> von Buttonstate abhängig
	:rtype: bool
	"""
	def durchlassen(self, currentplayer):
		return self.game.gelberbuttonstate

"""
stellt einen lilanen durchlässigen Stein dar, der durch Button gesteuert wird (Unterklasse von Buttonghostblock)
"""
class Lilaghostblock(Buttonghostblock):
	"""
	erstellt einen lilanen durchlässigen Stein und ruft dabei die init Funktion von Buttonghostblock auf
	:param fenster: gibt fenster-Surface weiter um darauf malen zu können
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
	malt den Block in die Fenster-Surface durch ein blit, abhängig davon ob der Button gedrückt ist oder nicht (anderes Bild)
	"""
	def draw(self):
		if self.game.lilabuttonstate:
			self.fenster.blit(self.ghostbild, (self.x * 30, self.y * 30))
		
		else:
			self.fenster.blit(self.bild, (self.x * 30, self.y * 30))
	
	"""
	gibt Durchlässigkeit des Steins an
	:param currentplayer: Spieler um den es geht
	:type currentplayer: player.Player
	:return: ob Stein durchlässig ist --> von Buttonstate abhängig
	:rtype: bool
	"""
	def durchlassen(self, currentplayer):
		return self.game.lilabuttonstate

"""
stellt einen roten durchlässigen Stein dar, der durch Button gesteuert wird (Unterklasse von Buttonghostblock)
"""
class Roterghostblock(Buttonghostblock):
	"""
	erstellt einen roten durchlässigen Stein und ruft dabei die init Funktion von Buttonghostblock auf
	:param fenster: gibt fenster-Surface weiter um darauf malen zu können
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
	malt den Block in die Fenster-Surface durch ein blit, abhängig davon ob der Button gedrückt ist oder nicht (anderes Bild)
	"""
	def draw(self):
		if self.game.roterbuttonstate:
			self.fenster.blit(self.bild, (self.x * 30, self.y * 30))
		
		else:
			self.fenster.blit(self.ghostbild, (self.x * 30, self.y * 30))
	
	"""
	gibt Durchlässigkeit des Steins an
	:param currentplayer: Spieler um den es geht
	:type currentplayer: player.Player
	:return: ob Stein durchlässig ist --> von Buttonstate abhängig
	:rtype: bool
	"""
	def durchlassen(self, currentplayer):
		#andersrum als bei gelb und lila: lässt nicht durch wenn gedrückt
		return not self.game.roterbuttonstate

"""
stellt einen rosanen für P1 durchlässigen Stein dar (Unterklasse von Ghostblock)
"""
class P1ghostblock(Ghostblock):
	"""
	erstellt einen rosanen durchlässigen Stein und ruft dabei die init Funktion von Playerghostblock auf
	:param fenster: gibt fenster-Surface weiter um darauf malen zu können
	:param x: x-Position des Blocks (zwischen 0 und 29)
	:param y: y-Position des Blocks (zwischen 0 und 19)
	:type fenster: pygame.display
	:type x: int
	:type y: int
	"""
	def __init__(self, fenster, x, y):
		super().__init__(fenster, x, y, "Bilder/rosablock.png")
	
	"""
	gibt Durchlässigkeit des Steins an
	:param currentplayer: Spieler um den es geht
	:type currentplayer: player.Player
	:return: ob Stein durchlässig ist --> vom jeweiligen Player abhängig
	:rtype: bool
	"""
	def durchlassen(self, currentplayer):
		return currentplayer.name == "p1"

"""
stellt einen schwarzen für P2 durchlässigen Stein dar (Unterklasse von Ghostblock)
"""
class P2ghostblock(Ghostblock):
	"""
	erstellt einen schwarzen durchlässigen Stein und ruft dabei die init Funktion von Playerghostblock auf
	:param fenster: gibt fenster-Surface weiter um darauf malen zu können
	:param x: x-Position des Blocks (zwischen 0 und 29)
	:param y: y-Position des Blocks (zwischen 0 und 19)
	:type fenster: pygame.display
	:type x: int
	:type y: int
	"""
	def __init__(self, fenster, x, y):
		super().__init__(fenster, x, y, "Bilder/schwarzerblock.png")
	
	"""
	gibt Durchlässigkeit des Steins an
	:param currentplayer: Spieler um den es geht
	:type currentplayer: player.Player
	:return: ob Stein durchlässig ist --> vom jeweiligen Player abhängig
	:rtype: bool
	"""
	def durchlassen(self, currentplayer):
		return currentplayer.name == "p2"
