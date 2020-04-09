import pygame
import player
#import readlevel
import block
#import sprung


pygame.init()


fenster = pygame.display.set_mode((900, 600))

pygame.display.set_caption("Mon jeu")


p1 = player.Player(800, 300, 38, 38, False, 5) #importiert die class Player aus der datei player
p2 = player.Player(100, 300, 28, 48, False, 5)# width und height 2 weniger da border width von rect = 2 und diese geht nach außen (s.u.)

bg = pygame.image.load("Background.jpeg")
blockbild = pygame.image.load("block.png")
run = True

def drawlevel(levelnumber):
	level = open("Level/Level"+ str(levelnumber) + ".txt")
	levelcounter_x = 1
	levelcounter_y = 1
	for line in level:
		for element in line: 
			if element == "5":
				fenster.blit(blockbild, (200, 200))
				print("H")
			levelcounter_x = levelcounter_x + 1
			levelcounter_y = int(levelcounter_x / 30)


def place():
	fenster.blit(blockbild, (200,200))


while run: #mainloop der alles mögliche zu jeder Zeit checkt
	pygame.time.delay(3) #clock (in milliseconds), pausiert das Programm für eine gewisse Zeit, also steht die Zahl für die Zeit, die verstreicht, bevor das Programm neu checkt


	for event in pygame.event.get(): #for every event out of the list of all the events happening
		if event.type == pygame.QUIT: #damit wenn man das Fenster zumacht, kein Error kommt
			run = False
			
	allkeys = pygame.key.get_pressed() #list of the status of all keys
		
		
	if not p1.springstate: #gleiches wie = False
		if allkeys[pygame.K_UP] :
			p1.springstate = True
	else:
		if p1.springzahl >= -5: #solange es 5 nicht erreicht
			if p1.springzahl > 0:
				neg = 1
			else:
				neg = -1
			p1.y = p1.y - ((p1.springzahl**2)*neg) #bewegung
			p1.springzahl = p1.springzahl - 2 #counter springzahl
		else: #variablen resetten wenn der sprung fertig ist
			p1.springstate = False
			p1.springzahl = 5
	if not p2.springstate: #gleiches wie = False
		if allkeys[pygame.K_w] :
			p2.springstate = True
	else: 
		if p2.springzahl >= -5:
			if p2.springzahl > 0:
				neg = 1
			else:
				neg = -1
			p2.y = p2.y - ((p2.springzahl**2)*neg) #neg weil es erst hoch dann runter muss
			p2.springzahl = p2.springzahl - 2
		else: #variablen resetten wenn der sprung fertig ist
			p2.springstate = False
			p2.springzahl = 5

	drawlevel(1)

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
	fenster.blit(player.papa, (p1.x, p1.y))
	fenster.blit(player.mama, (p2.x, p2.y))
	pygame.draw.rect(fenster, (0, 0, 255), p1.hitbox, 2) #fenster, farbe, koordinaten&size, border-width
	pygame.draw.rect(fenster, (0, 0, 255), p2.hitbox, 2)
	pygame.display.update()
	
pygame.quit()


