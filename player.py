import pygame
import block
import level

"""
stellt einen Spieler dar
"""
class Player():
	"""
	erstellt einen neuen Spieler
	:param width: Breite der Hitbox des Spielers
	:param height: Höhe der Hitbox des Spielers
	:param bildsource: path zur Bilddatei des Spielers
	:param fenster: übergibt fenster von main, um etwas malen zu können mit blit
	:param name: Name des Spielers (relevant für Becken: wer killt wen)
	:type width: int
	:type height: int
	:type bildsource: str
	:type fenster: pygame.display
	:type name: str
	"""
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
		self.springt = False
		
		self.darfspringen = True
		self.darffallen = True
		
		#um wv sich der Player gerne bewegen "möchte"
		self.bew_x = 0
		self.bew_y = 0
		
		self.geschw = 1
		
		self.zielstate = False
		self.isdead = False
	
	"""
	stellt die Position des Spielers(self) wieder auf die Standard-Werte aus der Level-Datei
	"""
	def reset(self):
		self.x = self.standard_x
		self.y = self.standard_y
		self.isdead = False
		self.zielstate = False
	
	"""
	malt den jeweiligen Spieler in die Fenster-Surface durch ein blit
	"""
	def draw(self):
		self.fenster.blit(self.bild, (self.x, self.y))
	
	"""
	isdead-variable wird  aktiv
	"""
	def die(self):
		self.isdead = True
	
	"""
	führt die horizontale und vertikale Bewegung des Spielers aus
	prüft davor die Kollisionen
	:param key_left: Taste Links/d ist gedrückt
	:param key_right: Taste Rechts/a ist gedrückt
	:param key_up: Taste Oben/w ist gedrückt
	:param level: gibt aktuelles Level (die Blöcke) weiter um die Kollisionen zu testen
	:type key_left: bool
	:type key_right: bool
	:type key_up: bool
	:type level: level.Level
	"""
	def bew(self, key_left, key_right, key_up, level):
		#horizontale Bewegung
		if key_left:
			self.bew_x = -self.schritt
		
		elif key_right:
			self.bew_x = self.schritt
		#verlangsamt den Player (bsp Becken)
		self.bew_x = self.bew_x * self.geschw
		#vertikale Bewegung --> springt nur hoch!
		if not self.springt and self.darfspringen and key_up:
			self.darfspringen = False
			self.springt = True
		
		if self.springt:

			#parabelförmiger Sprung
			if self.springzahl > 0:
				self.bew_y = -(self.springzahl**2)
				self.springzahl = self.springzahl - 1
				self.darffallen = False
			
			else:
				#alles resetten wenn der Sprung fertig ist
				self.springt = False
				self.springzahl = 6.75
				self.darffallen = True

		self.geschw = 1
		
		#die tatsächliche Bewegung wird erst hier ausgeführt
		if not level.collision(self):
			self.y = (self.y + self.bew_y) % 600
			self.x = (self.x + self.bew_x) % 900
		
		self.bew_x = 0
		self.bew_y = 0
	
	"""
	Gravitation
	fällt so lange bis er eine Kollision hat (erst wenn Sprung abgeschlossen ist)
	:param level: aktuelles Level
	:type level: level.Level
	"""
	def grav(self, level):
		#wenn ich springe darf ich nicht gleichzeitig fallen
		if self.darffallen:
			
			#die Bewegung muss in 4 kleinen Schritten ausgeführt werden damit es unmöglich ist durch einen Block "durchzufallen"
			for x in range(4):
				self.bew_y = (self.fallzahl**2) / 4
				
				if not level.collision(self):
					self.y = (self.y + self.bew_y) % 600
				
				else:
					self.fallzahl = 1
					self.bew_y = 0
					self.darfspringen = True
					break #damit er nicht 4 mal durch den Loop geht wenn er eh auf dem Boden steht
			
			#damit er nicht um immer mehr nach unten fällt
			if self.fallzahl < 6:
				self.fallzahl = self.fallzahl + 1
