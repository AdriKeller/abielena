import pygame
import block
import level

#stellt einen Spieler dar
class Player(object):
	
	#erstellt einen neuen Spieler
	#Parameter:
	#width und height: Breite und Höhe der Hitbox des Spielers
	#bildsource: path zur Bilddatei des Spielers
	#fenster: übergibt fenster von main, um etwas malen zu können mit blit
	#name: Name des Spielers (relevant für Becken: wer killt wen)
	def __init__(self, width, height, bildsource, fenster, name):
		
		self.x = 0
		self.y = 0
		
		self.standard_x = 0
		self.standard_y = 0
		
		self.width = width
		self.height = height
		
		self.fenster = fenster
		
		self.bild = pygame.image.load(bildsource)
		
		self.name = name
		
		self.schritt = 10
		
		self.springzahl = 6.75
		self.fallzahl = 1
		
		self.darfspringen = True
		self.darffallen = True
		
		#um wv sich der Player gerne bewegen "möchte"
		self.bew_x = 0
		self.bew_y = 0
		
		self.zielstate = False
	
	#stellt die Position des Spielers(self) wieder auf die Standard-Werte aus der Level-Datei
	def reset(self):
		self.x = self.standard_x
		self.y = self.standard_y
		self.zielstate = False
	
	#malt den jeweiligen Spieler in die Fenster-Surface durch ein blit
	def draw(self):
		self.fenster.blit(self.bild, (self.x, self.y))
	
	#führt die horizontale und vertikale Bewegung des Spielers aus
	#prüft davor die Kollisionen
	#Parameter: 
	#keys: Booleans, die angeben ob die jeweilige Taste gedrückt ist (Rechts/a, Links/d, Oben/w)
	#level: gibt aktuelles Level (die Blöcke) weiter um die Kollisionen zu testen
	def bew(self, key_left, key_right, key_up, level):
		#horizontale Bewegung
		if key_left:
			self.bew_x = - self.schritt
		elif key_right:
			self.bew_x = self.schritt
		
		#vertikale Bewegung --> springt nur hoch!
		if self.darfspringen:
			
			if key_up:
				self.darfspringen = False #TO DO
		else:
			
			#parabelförmiger Sprung
			if self.springzahl > 0:
				self.bew_y = -(self.springzahl**2)
				self.springzahl = self.springzahl - 1
				self.darffallen = False
				
			else:
				#alles resetten wenn der Sprung fertig ist
				self.darfspringen = True
				self.springzahl = 6.75
				self.darffallen = True
		
		#die tatsächliche Bewegung wird erst hier ausgeführt
		if not level.collision(self, level):
			self.y = self.y + self.bew_y
			self.x = self.x + self.bew_x
			
		self.bew_x = 0
		self.bew_y = 0
	
	#Gravitation
	#fällt so lange bis er eine Kollision hat (erst wenn Sprung abgeschlossen ist)
	def grav(self, level):
		if self.darffallen: #wenn ich springe darf ich nicht gleichzeitig fallen
			
			#die Bewegung muss in 4 kleinen Schritten ausgeführt werden damit es unmöglich ist durch einen Block "durchzufallen"
			for x in range(4):
				self.bew_y = (self.fallzahl**2)/4
				
				if not level.collision(self, level):
					self.darfspringen = False
					self.y = self.y + self.bew_y
					self.darfspringen = True
					
				else:
					self.fallzahl = 1
					self.bew_y = 0
					
			if self.fallzahl < 6: #damit er nicht um immer mehr nach unten fällt
					self.fallzahl = self.fallzahl + 1
