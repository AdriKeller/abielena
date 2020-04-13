import pygame
import player


class Block(object):
	
	def __init__(self, fenster, x, y, bildsource):
		self.fenster = fenster
		self.x = x
		self.y = y
		self.bild = pygame.image.load(bildsource)
		self.height = 30
		self.width = 30
		
	def draw(self):
		self.fenster.blit(self.bild, (self.x*30, self.y*30))
		
	def collbecken(self, currentplayer, level): #schaut ob collision mit becken, wenn ja tötet
		if self.kills(currentplayer):
			level.die()
	
	#def collziel(self, currentplayer, level):
		#if (self.width * self.x < currentplayer.x + currentplayer.bew_x + currentplayer.width) and (currentplayer.x + currentplayer.bew_x < self.width * (self.x + 1)) and (self.height * (self.y + tiefe)  < currentplayer.y + currentplayer.bew_y + currentplayer.height) and (currentplayer.y + currentplayer.bew_y < self.height * (self.y + 1)):

		
	def collision(self, currentplayer, level): #currentplayer = alles vom player
		tiefe = 0 #sagt wv tiefer von der oberen kante die Hitbox anfängt
		currentplayer.schritt = 10
		if isinstance(self, Becken):
			tiefe = 2/3
			currentplayer.schritt = 3
		#if isinstance(self, Door):
			#self.collziel(currentplayer, level)
		#	return False
		elif (self.width * self.x < currentplayer.x + currentplayer.bew_x + currentplayer.width) and (currentplayer.x + currentplayer.bew_x < self.width * (self.x + 1)) and (self.height * (self.y + tiefe)  < currentplayer.y + currentplayer.bew_y + currentplayer.height) and (currentplayer.y + currentplayer.bew_y < self.height * (self.y + 1)):
			self.collbecken(currentplayer, level)
			return True
		else:
			return False




class Stein(Block):
	def __init__(self, fenster, x, y):
		super().__init__(fenster, x, y, "block.png")

	def kills(self, currentplayer):
		return False



class Ziel(Block):
	def __init__(self, fenster, x, y, bildsource):
		super().__init__(fenster, x, y, bildsource)
		self.height = 60
	
	def win(self, currentplayer):
		return False
		
	def kills(self, currentplayer):
		return False
		
class P1ziel(Ziel):#rosa Tür
	def __init__(self, fenster, x, y):
		super().__init__(fenster, x, y, "p1ziel.png")
	
	def win(self, currentplayer): #wenn rosa Spieler, dann True
		return currentplayer.name == "p1"
		

class P2ziel(Ziel): #schwarze Tür
	def __init__(self, fenster, x, y):
		super().__init__(fenster, x, y, "p2ziel.png")
	
	def win(self, currentplayer):
		return currentplayer.name == "p2" #wenn schwarzer Spieler, dann True

class Becken(Block):
	def __init__(self, fenster, x, y, bildsource):
		super().__init__(fenster, x, y, bildsource)
		
	def kills(self, currentplayer):
		return False


class P1becken(Becken):#rosa Becken
	def __init__(self, fenster, x, y):
		super().__init__(fenster, x, y, "p1becken.png")
	
	def kills(self, currentplayer):
		return currentplayer.name == "p2" # wenn schwarzer Spieler, dann True
	
class P2becken(Becken): #schwarzes Becken
	def __init__(self, fenster, x, y):
		super().__init__(fenster, x, y, "p2becken.png")
		
	def kills(self, currentplayer):
		return currentplayer.name == "p1"  #wenn rosa Spieler, dann True
		

class Bothbecken(Becken):
	def __init__(self, fenster, x, y):
		super().__init__(fenster, x, y, "bothbecken.png")
		
	def kills(self, currentplayer): #tötet immer
		return True




