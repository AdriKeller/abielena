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
		
	def collision(self, currentplayer, level): #currentplayer = alles vom player  
		if (self.width * self.x < currentplayer.x + currentplayer.bew_x + currentplayer.width) and (currentplayer.x + currentplayer.bew_x < self.width * (self.x + 1)) and (self.height * self.y < currentplayer.y + currentplayer.bew_y + currentplayer.height) and (currentplayer.y + currentplayer.bew_y < self.height * (self.y + 1)):
			self.collide(currentplayer, level)
			return True
		else:
			return False





class Stein(Block):
	def __init__(self, fenster, x, y):
		super().__init__(fenster, x, y, "block.png")

		
		
def collide(self, currentplayer, level): #schaut ob collision mit becken, wenn ja tötet
	#print(self.kills(currentplayer))
	if self.kills(currentplayer):
		level.die()


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



