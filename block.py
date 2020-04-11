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
		
	def collision(self, currentplayer, level): #currentplayer = alles vom player  #bew = +-1 rechts/links
		if (Block.width * self.x < currentplayer.x + currentplayer.bew_x + currentplayer.width) and (currentplayer.x + currentplayer.bew_x < Block.width * (self.x + 1)) and (Block.height * self.y < currentplayer.y + currentplayer.bew_y + currentplayer.height) and (currentplayer.y + currentplayer.bew_y < Block.height * (self.y + 1)):
			self.collide(currentplayer, level)
			return True
		else:
			return False
	
	def collide(self, currentplayer, level):
		pass
			
class Stein(Block):
	def __init__(self, fenster, x, y):
		super().__init__(fenster, x, y, "block.png")


class Becken(Block):
	def __init__(self, fenster, x, y, bildsource):
		super().__init__(fenster, x, y, bildsource)
		
	def collide(self, currentplayer, level):
		print(self.kills(currentplayer))
		if self.kills(currentplayer):
			level.die()
	
	def kills(self, currentplayer):
		pass

class P1becken(Becken):
	def __init__(self, fenster, x, y):
		super().__init__(fenster, x, y, "p1becken.png")
	
	def kills(self, currentplayer):
		return currentplayer.name == "p2"
		

class P2becken(Becken):
	def __init__(self, fenster, x, y):
		super().__init__(fenster, x, y, "p2becken.png")
	
	def kills(self, currentplayer):
		return currentplayer.name == "p1"
		

class Bothbecken(Becken):
	def __init__(self, fenster, x, y):
		super().__init__(fenster, x, y, "bothbecken.png")
	
	def kills(self, currentplayer):
		return True



