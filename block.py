import pygame
import player

#stellt einen einzelnen Block dar (Steine, Becken, Zieltüren, ...)
class Block(object):
	#erstelle einen neuen Block
	#Parameter:
	#fenster: gibt fenster-Surface weiter um darauf malen zu können
	#x und y:  x und y -Position des Blocks (x€[0:30] y€[0:20])
	#bildsource: path zur Bilddatei des Blocks
	def __init__(self, fenster, x, y, bildsource):
		
		self.fenster = fenster
		
		self.x = x
		self.y = y
		
		self.height = 30
		self.width = 30
		
		self.bild = pygame.image.load(bildsource)
		
	#malt den jeweiligen Block in die Fenster-Surface durch ein blit
	def draw(self):
		self.fenster.blit(self.bild, (self.x*30, self.y*30))
	
	#testet ob der Block für den jeweiligen Spieler tödlich ist
	#Parameter:
	#currentplayer: SPieler um den es geht
	def kills(self, currentplayer):
		return False
	
	#löst das Sterben aus
	#Parameter: 
	#currentplayer: Spieler um den es geht
	#level: das aktuelle Level um die die()-methode auszulösen
	def collbecken(self, currentplayer, level): #schaut ob der collisions-block den spieler tötet
		if self.kills(currentplayer):
			level.die()
	
	#Legt fest ob der Spieler in seiner Zieltür ist
	#Parameter:
	#currentplayer: Spieler um den es geht
	#level: das aktuelle Level
	def collziel(self, currentplayer):
		if self.wins(currentplayer):
			currentplayer.zielstate = True
			
		else: 
			currentplayer.zielstate = False
		
	def collision(self, currentplayer, level): #currentplayer = alles vom player
		tiefe = 0 #sagt wv tiefer von der oberen kante die Hitbox anfängt
		currentplayer.schritt = 10
		if isinstance(self, Becken):
			tiefe = 2/3
			currentplayer.schritt = 3
		
		if (self.width * self.x < currentplayer.x + currentplayer.bew_x + currentplayer.width) and (currentplayer.x + currentplayer.bew_x < self.width * (self.x + 1)) and (self.height * (self.y + tiefe)  < currentplayer.y + currentplayer.bew_y + currentplayer.height) and (currentplayer.y + currentplayer.bew_y < self.height * (self.y + 1)):
			if currentplayer.bew_y > 0: #wenn er sich nach unten bewegt
				self.collbecken(currentplayer, level)
			return True
		else:
			return False

#stellt einen Stein dar (Unterklasse Block)
class Stein(Block):
	#erstellt einen neuen Stein und ruft dabei die init funktion von Block auf
	def __init__(self, fenster, x, y):
		super().__init__(fenster, x, y, "block.png")
		
#stellt eine Zieltür dar (Unterklasse Block)
class Ziel(Block):
	#erstellt eine neuen Zieltür und ruft dabei die init funktion von Block auf
	def __init__(self, fenster, x, y, bildsource):
		super().__init__(fenster, x, y, bildsource)
		
		self.height = 60
		self.width = 30
	
	#Elemente der Klasse Ziel lassen einen Spieler grundsätzlich nicht gewinnen
	def wins(self, currentplayer):
		return False

#stellt die Zieltür für den ersten Player dar(rosa)
class P1ziel(Ziel):
	#erstellt die rosa Zieltür und ruft dabei die init funktion von Zieltür auf: setzt den Path für die Bilddatei 
	def __init__(self, fenster, x, y):
		super().__init__(fenster, x, y, "p1ziel.png")
	
	#Elemente der Klasse Ziel lassen den Spieler 1 gewinnen
	def wins(self, currentplayer):
		return currentplayer.name == "p1"

#stellt die Zieltür für den zewiten Player dar (schwarz)
class P2ziel(Ziel): #schwarze Tür
	#erstellt die rosa Zieltür und ruft dabei die init funktion von Zieltür auf: setzt den Path für die Bilddatei 
	def __init__(self, fenster, x, y):
		super().__init__(fenster, x, y, "p2ziel.png")
	
	#Elemente der Klasse Ziel lassen den Spieler 2 gewinnen
	def wins(self, currentplayer):
		return currentplayer.name == "p2" #wenn schwarzer Spieler, dann True


#stellt ein Becken dar
class Becken(Block):
	#erstellt ein neues Becken und ruft dabei die init funktion von Block aus
	def __init__(self, fenster, x, y, bildsource):
		super().__init__(fenster, x, y, bildsource)
	
	#Elemente dieser Klasse sind grundsäzulich nicht töter für die Spieler
	def kills(self, currentplayer):
		return False

#stellt ein Becken der Farbe des Spieler 1 dar (rosa)
class P1becken(Becken):
	#erstellt ein neues Becken der Farbe Spieler 1 und ruft dabei die init Funktion von Becken auf: setzt den path für die Bilddatei
	def __init__(self, fenster, x, y):
		super().__init__(fenster, x, y, "p1becken.png")
	
	#Elemente dieser Klasse töten den Spieler namens p2
	def kills(self, currentplayer):
		return currentplayer.name == "p2"

#stellt ein Becken der Farbe des Spieler 2 dar (schwarz)
class P2becken(Becken):
	#erstellt ein neues Becken der Farbe Spieler 2 und ruft dabei die init Funktion von Becken auf: setzt den path für die Bilddatei
	def __init__(self, fenster, x, y):
		super().__init__(fenster, x, y, "p2becken.png")
		
	#Elemente dieser Klasse töten den Spieler namens p1
	def kills(self, currentplayer):
		return currentplayer.name == "p1"  #wenn rosa Spieler, dann True
#stellt ein giftiges Becken dar (grün)
class Bothbecken(Becken):
	#erstellt ein neues Becken der Farbe giftig und ruft dabei die init Funktion von Becken auf: setzt den path für die Bilddatei
	def __init__(self, fenster, x, y):
		super().__init__(fenster, x, y, "bothbecken.png")
	
	#Elemente dieser Klasse sind immer tödlich
	def kills(self, currentplayer):
		return True
