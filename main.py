import pygame
from player import Player
pygame.init()


fenster = pygame.display.set_mode((1000, 650))

pygame.display.set_caption("Mon jeu")


p1 = Player(900, 550) #importiert die class Player aus der datei player
p2 = Player(100, 550)


run = True
	


while run: #mainloop der alles mögliche zu jeder Zeit checkt
	pygame.time.delay(3) #clock (in milliseconds), pausiert das Programm für eine gewisse Zeit, also steht die Zahl für die Zeit, die verstreicht, bevor das Programm neu checkt


	for event in pygame.event.get(): #for every event out of the list of all the events happening
		if event.type == pygame.QUIT: #damit wenn man das Fenster zumacht, kein Error kommt
			run = False
			
	allkeys = pygame.key.get_pressed() #list of the status of all keys
		
		
		
	if allkeys[pygame.K_LEFT]:
		p1.bew(-1)
	if allkeys[pygame.K_RIGHT]:
		p1.bew(1)
	if allkeys[pygame.K_a]:
		p2.bew(-1)
	if allkeys[pygame.K_d]:
		p2.bew(1)
	
	fenster.fill(0, 0, 0)
	pygame.draw.rect(fenster, (255, 0, 0), (p1.x, p1.y, p1.width, p1.height))
	pygame.draw.rect(fenster, (0, 0, 255), (p2.x, p2.y, p2.width, p2.height))
	pygame.display.update()
	
pygame.quit()
