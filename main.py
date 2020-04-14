import pygame
import player
import level
import block


pygame.init()


fenster = pygame.display.set_mode((900, 600))

pygame.display.set_caption("Mon jeu")

pygame.font.init() 
fontdie = pygame.font.SysFont('Comic Sans MS', 50) #schriftart festlegen
fontwin = pygame.font.SysFont('Comic Sans MS', 50)

dietext = fontdie.render('Du bist gestorben', False, (255, 255, 255))
wintext = fontwin.render('Du hast gewonnen!!', False, (255, 0, 0))

p1 = player.Player(800, 532, 38, 38, "barbapapa.png", fenster, "p1") #importiert die class Player aus der datei player
p2 = player.Player(500, 522, 28, 48, "barbamama.gif", fenster, "p2")# width und height 2 weniger da border width von rect = 2 und diese geht nach außen (s.u.) --> für hitbox

bg = pygame.image.load("Background.jpeg")

run = True

levelnumber = 1 #das aktuelle Level festlegen
levelact = level.Level(fenster, levelnumber) 

while run: #mainloop der alles mögliche zu jeder Zeit checkt
	pygame.time.delay(3) #clock (in milliseconds), pausiert das Programm für eine gewisse Zeit, also steht die Zahl für die Zeit, die verstreicht, bevor das Programm neu checkt


	for event in pygame.event.get(): #for every event out of the list of all the events happening
		if event.type == pygame.QUIT: #damit wenn man das Fenster zumacht, kein Error kommt
			run = False
			
	allkeys = pygame.key.get_pressed() #list of the status of all keys
		

		
	p1.bew(allkeys[pygame.K_LEFT], allkeys[pygame.K_RIGHT], allkeys[pygame.K_UP], levelact)
	p2.bew(allkeys[pygame.K_a], allkeys[pygame.K_d], allkeys[pygame.K_w], levelact)
	p1.grav(levelact)
	p2.grav(levelact)


	fenster.blit(bg, (0, 0))
	levelact.draw_background()
	p1.draw()
	p2.draw()
	levelact.draw_foreground()
	if levelact.leveldeath:
		fenster.fill((0, 0, 0))
		fenster.blit(dietext, (400, 300))
	elif p1.zielstate and p2.zielstate:
		fenster.fill((255, 212, 0))
		fenster.blit(wintext, (400, 300))
	pygame.display.update()
	
pygame.quit()


