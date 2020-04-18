import pygame
import player

"""
stellt einen einzelnen Block dar
"""
class Block(object):
	"""
	erstelle einen neuen Block
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
		self.fenster = fenster
		
		self.x = x
		self.y = y
		
		self.height = 30
		self.width = 30
		
		self.bild = pygame.image.load(bildsource)
	
	"""
	malt den jeweiligen Block in die Fenster-Surface durch ein blit
	"""
	def draw(self):
		self.fenster.blit(self.bild, (self.x * 30, self.y * 30))
	
	"""
	Testet die Kollision zwischen dem Block und dem jeweiligen Spieler
	:param currentplayer: Spieler um den es geht
	:type currentplayer: player.Player
	:return: Gab es eine Kollision zwischen dem Player und dem Block
	:rtype: bool
	"""
	def collision(self, currentplayer):
		return ((self.width * self.x < currentplayer.x + currentplayer.bew_x + currentplayer.width) and (currentplayer.x + currentplayer.bew_x < self.width * (self.x + 1)) and (self.height * self.y  < currentplayer.y + currentplayer.bew_y + currentplayer.height) and (currentplayer.y + currentplayer.bew_y < self.height * (self.y + 1)))
	
	"""
	
	"""
	def handleCollision(self, currentplayer):
		return True #behandle diesen Block als sei er ein massiver Stein
