import pygame
import player
import level
import block


pygame.init()


fenster = pygame.display.set_mode((900, 600))

pygame.display.set_caption("Mon jeu")


p1 = player.Player(800, 532, 38, 38) #importiert die class Player aus der datei player
p2 = player.Player(100, 522, 28, 48)# width und height 2 weniger da border width von rect = 2 und diese geht nach außen (s.u.) --> für hitbox

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
		


	p1.jump(allkeys[pygame.K_UP])
	p2.jump(allkeys[pygame.K_w])	
		
	p1.bew(allkeys[pygame.K_LEFT], allkeys[pygame.K_RIGHT], allkeys[pygame.K_UP], levelact)
	p2.bew(allkeys[pygame.K_a], allkeys[pygame.K_d], allkeys[pygame.K_w], levelact)


	fenster.fill((255, 255, 255))
	fenster.blit(bg, (0, 0))
	fenster.blit(player.papa, (p1.x, p1.y))
	fenster.blit(player.mama, (p2.x, p2.y))
	levelact.draw()
	#pygame.draw.rect(fenster, (0, 0, 255), p1.hitbox, 2) #fenster, farbe, koordinaten&size, border-width
	#pygame.draw.rect(fenster, (0, 0, 255), p2.hitbox, 2)
	pygame.display.update()
	
pygame.quit()


