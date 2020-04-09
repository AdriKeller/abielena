import pygame
import player
import readlevel
import block
import sprung

pygame.init()
fenster = pygame.display.set_mode((900, 600))
pygame.display.set_caption("Mon jeu")

p1 = player.Player(800, 300, 38, 38, False, 5) #importiert die class Player aus der datei player
p2 = player.Player(100, 300, 28, 48, False, 5)# width und height 2 weniger da border width von rect = 2 und diese geht nach außen (s.u.)

bg = pygame.image.load("Background.jpeg")

level = readlevel.Level(1, fenster)

run = True
while run: #mainloop der alles mögliche zu jeder Zeit checkt
	pygame.time.delay(3) #clock (in milliseconds), pausiert das Programm für eine gewisse Zeit, also steht die Zahl für die Zeit, die verstreicht, bevor das Programm neu checkt

	for event in pygame.event.get(): #for every event out of the list of all the events happening
		if event.type == pygame.QUIT: #damit wenn man das Fenster zumacht, kein Error kommt
			run = False
	
	allkeys = pygame.key.get_pressed() #list of the status of all keys

	sprung.jump(p1, allkeys[pygame.K_UP])
	sprung.jump(p2, allkeys[pygame.K_w])

	if allkeys[pygame.K_LEFT]:
		p1.bew(-1)
	if allkeys[pygame.K_RIGHT]:
		p1.bew(1)
	if allkeys[pygame.K_a]:
		p2.bew(-1)
	if allkeys[pygame.K_d]:
		p2.bew(1)
	
	fenster.fill((255, 255, 255))
	fenster.blit(bg, (0, 0))
	level.draw()
	#readlevel.Level(1, fenster)

	fenster.blit(player.papa, (p1.x, p1.y))
	fenster.blit(player.mama, (p2.x, p2.y))

	pygame.draw.rect(fenster, (0, 0, 255), p1.hitbox, 2) #fenster, farbe, koordinaten&size, border-width
	pygame.draw.rect(fenster, (0, 0, 255), p2.hitbox, 2)

	pygame.display.update()
	
pygame.quit()


