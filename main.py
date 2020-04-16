import pygame
import player
import level
import block
import os
import time

pygame.init()

fenster = pygame.display.set_mode((900, 600))

pygame.display.set_caption("Mon jeu")

p1 = player.Player(26, 50, "barbapapa.png", fenster, "p1") #importiert die class Player aus der datei player
p2 = player.Player(26, 50, "barbamama.png", fenster, "p2")# width und height 2 weniger da border width von rect = 2 und diese geht nach außen (s.u.) --> für hitbox

bg = pygame.image.load("Background.jpeg")
bgdie = pygame.image.load("Background_die.jpeg")
bgwin = pygame.image.load("Background_win.jpeg")
finishlevel = pygame.image.load("Background_finishlevel.jpeg")

levelnumber = 1
levelact = level.Level(fenster, levelnumber, p1, p2)

p1.reset()
p2.reset()

run = True 

while run:
	pygame.time.delay(3) #clock in milliseconds --> Zeit nachdem Loop neu startet
		
	for event in pygame.event.get(): #for every event out of the list of all the events happening
		if event.type == pygame.QUIT: #Loop unterbrechen wenn Fenster geschlossen wird
			run = False

	allkeys = pygame.key.get_pressed() #Liste mit Status aller Tasten
		
	p1.bew(allkeys[pygame.K_LEFT], allkeys[pygame.K_RIGHT], allkeys[pygame.K_UP], levelact)
	p2.bew(allkeys[pygame.K_a], allkeys[pygame.K_d], allkeys[pygame.K_w], levelact)
	
	p1.grav(levelact)
	p2.grav(levelact)
	
	fenster.blit(bg, (0, 0))
	
	if levelnumber == 0: #wenn es sich um das finale Level handelt 
		fenster.blit(finishlevel, (0, 0))
	
	#alles auf die Surface malen (Blöcke, Figuren)
	levelact.draw_background()
	p1.draw()
	p2.draw()
	levelact.draw_foreground()
	
	if levelact.leveldeath:
		#time.sleep(0.5)
		fenster.blit(bgdie, (0, 0))
		
		if  allkeys[pygame.K_SPACE]: #Level von neuem beginnen
			levelact.leveldeath = False
			
			p1.reset()
			p2.reset()
			
	elif p1.zielstate and p2.zielstate:
		#time.sleep(0.5)
		fenster.blit(bgwin, (0, 0))
		
		if allkeys[pygame.K_SPACE]: #in nächstes Level übergehen
			levelnumber = levelnumber + 1
			
			if os.path.isfile("Level/Level"+ str(levelnumber) + ".txt"): #testen ob es die Datei gibt
				levelact = level.Level(fenster, levelnumber, p1, p2)
				
			else:
				levelnumber = 0
				levelact = level.Level(fenster, levelnumber, p1, p2)
				
			p1.reset() 
			p2.reset()
			
	pygame.display.update()
	
pygame.quit()
