import pygame
import player
import level
import block
import os

pygame.init()
fenster = pygame.display.set_mode((900, 600))
pygame.display.set_caption("Barbasauteur")

p1 = player.Player(26, 50, "Bilder/barbapapa.png", fenster, "p1")
p2 = player.Player(26, 50, "Bilder/barbamama.png", fenster, "p2")

bg = pygame.image.load("Bilder/Background.jpeg")
bgdie = pygame.image.load("Bilder/Background_die.jpeg")
bgwin = pygame.image.load("Bilder/Background_win.jpeg")
finishlevel = pygame.image.load("Bilder/Background_finishlevel.jpeg")

buttonstate = [False, False, False]

levelnumber = 5
levelact = level.Level(fenster, levelnumber, p1, p2, buttonstate)
p1.reset()
p2.reset()


run = True
while run:
	#clock in milliseconds --> Zeit nachdem Loop neu startet
	pygame.time.delay(3)
	
	#for every event out of the list of all the events happening
	for event in pygame.event.get():
		
		#Loop unterbrechen wenn Fenster geschlossen wird
		if event.type == pygame.QUIT:
			run = False

	#Liste mit Status aller Tasten
	allkeys = pygame.key.get_pressed()
	
	if p1.isdead or p2.isdead:
		fenster.blit(bgdie, (0, 0))
		
		#Level von neuem beginnen
		if  allkeys[pygame.K_SPACE]:
			p1.reset()
			p2.reset()
		
		else:
			pygame.display.update()
			continue
	
	elif p1.zielstate and p2.zielstate:
		fenster.blit(bgwin, (0, 0))
		
		#in nächstes Level übergehen
		if allkeys[pygame.K_SPACE]:
			levelnumber = levelnumber + 1
			
			#testen ob es die Datei gibt
			if os.path.isfile("Level/Level"+ str(levelnumber) + ".txt"):
				levelact = level.Level(fenster, levelnumber, p1, p2, buttonstate)
			
			else:
				levelnumber = 0
				levelact = level.Level(fenster, levelnumber, p1, p2, buttonstate)
			
			p1.reset()
			p2.reset()
		
		else:
			pygame.display.update()
			continue
	
	p1.bew(allkeys[pygame.K_LEFT], allkeys[pygame.K_RIGHT], allkeys[pygame.K_UP], levelact)
	p2.bew(allkeys[pygame.K_a], allkeys[pygame.K_d], allkeys[pygame.K_w], levelact)
	
	p1.grav(levelact)
	p2.grav(levelact)
	
	fenster.blit(bg, (0, 0))
	
	#wenn es sich um das finale Level handelt
	if levelnumber == 0:
		fenster.blit(finishlevel, (0, 0))
	
	#alles auf die Surface malen (Blöcke, Figuren)
	levelact.draw_background()
	p1.draw()
	p2.draw()
	levelact.draw_foreground()
	
	pygame.display.update()

pygame.quit()
