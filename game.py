import pygame
import player
import level
import os

"""
stellt das Spiel dar
"""
class Game():
	"""
	erstelle ein neues Spiel
	"""
	def __init__(self):
		pygame.init()
		self.fenster = pygame.display.set_mode((900, 600))
		pygame.display.set_caption("Barbasauteur")
		
		self.p1 = player.Player(26, 50, "Bilder/barbapapa.png", self.fenster, "p1")
		self.p2 = player.Player(26, 50, "Bilder/barbamama.png", self.fenster, "p2")
		
		self.bgdie = pygame.image.load("Bilder/die.png")
		self.bgwin = pygame.image.load("Bilder/win.png")
		self.finishlevel = pygame.image.load("Bilder/finishlevel.png")
		
		self.levelnumber = 1
		self.levelact = level.Level(self)
		
		self.p1.reset()
		self.p2.reset()
		
		runstate = True
		while runstate:
			#clock in milliseconds --> Zeit nachdem Loop neu startet
			pygame.time.delay(3)
			
			#for every event out of the list of all the events happening
			for event in pygame.event.get():
				
				#Loop unterbrechen wenn Fenster geschlossen wird
				if event.type == pygame.QUIT:
					runstate = False
			
			self.roterbuttonstate = False
			self.lilabuttonstate = False
			self.gelberbuttonstate = False

			#Liste mit Status aller Tasten
			allkeys = pygame.key.get_pressed()
			
			if self.p1.isdead or self.p2.isdead:
				self.fenster.blit(self.levelact.bg, (0,0))
				self.fenster.blit(self.bgdie, (0, 0))
				
				#Level von neuem beginnen
				if  allkeys[pygame.K_SPACE]:
					self.p1.reset()
					self.p2.reset()
				
				else:
					pygame.display.update()
					continue
			
			elif self.p1.zielstate and self.p2.zielstate:
				self.fenster.blit(self.levelact.bg, (0,0))
				self.fenster.blit(self.bgwin, (0, 0))
				
				#in naechstes Level uebergehen
				if allkeys[pygame.K_SPACE]:
					self.levelnumber = self.levelnumber + 1
					
					#testen ob es die Datei gibt
					if os.path.isfile("Level/Level"+ str(self.levelnumber) + ".txt"):
						self.levelact = level.Level(self)
					
					else:
						self.levelnumber = 0
						self.levelact = level.Level(self)
					
					self.p1.reset()
					self.p2.reset()
				
				else:
					pygame.display.update()
					continue

			self.levelact.collision(self.p1)
			self.levelact.collision(self.p2)
			
			self.p1.bew(allkeys[pygame.K_LEFT], allkeys[pygame.K_RIGHT], allkeys[pygame.K_UP], self.levelact)
			self.p2.bew(allkeys[pygame.K_a], allkeys[pygame.K_d], allkeys[pygame.K_w], self.levelact)
			
			self.p1.grav(self.levelact)
			self.p2.grav(self.levelact)
			
			self.fenster.blit(self.levelact.bg, (0, 0))
			
			#wenn es sich um das finale Level handelt
			if self.levelnumber == 0:
				self.fenster.blit(self.levelact.bg, (0,0))
				self.fenster.blit(self.finishlevel, (0, 0))
			
			#alles auf die Surface malen (Bloecke, Figuren)
			self.levelact.draw_background()
			self.p1.draw()
			self.p2.draw()
			self.levelact.draw_foreground()
			
			pygame.display.update()
		pygame.quit()
