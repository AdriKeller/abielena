import pygame
import player


class Block(object):
	height = 30
	width = 30
	
	def __init__(self, fenster, x, y, bildsource):
		self.fenster = fenster
		self.x = x
		self.y = y
		self.bild = pygame.image.load(bildsource)
		
	def draw(self):
		self.fenster.blit(self.bild, (self.x*30, self.y*30))
		
	def collision(self, currentplayer, bew): #currentplayer = alles vom player  #bew = +-1 rechts/links
		if bew > 0: #wenn Player nach rechts läuft
			if self.x*30 < currentplayer.x + player.Player.schritt + currentplayer.width: #Achtung self.x ist zwsichen 0 und 30!
				return True
			else:
				return False
		elif bew < 0: #wenn Player nach links läuft
			if self.x*30 + 30 > currentplayer.x - player.Player.schritt:
				return True
			else:
				return False
		
		
		
		
class Stein(Block):
	def __init__(self, fenster, x, y):
		super().__init__(fenster, x, y, "block.png")


class Becken(Block):
	def __init__(self, fenster, x, y, bildsource):
		super().__init__(fenster, x, y, bildsource)
		


class P1becken(Becken):
	def __init__(self, fenster, x, y):
		super().__init__(fenster, x, y, "p1becken.png")
		

class P2becken(Becken):
	def __init__(self, fenster, x, y):
		super().__init__(fenster, x, y, "p2becken.png")
		

class Bothbecken(Becken):
	def __init__(self, fenster, x, y):
		super().__init__(fenster, x, y, "bothbecken.png")

