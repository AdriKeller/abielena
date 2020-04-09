import pygame
import block
x = 0
y = 0
block1 = pygame.image.load("block.png")
def drawlevel(levelnumber, fenster):
	level = open("Level/Level"+ str(levelnumber) + ".txt")
	levelcounter_x = 0
	levelcounter_y = 0
	for line in level:
		for element in line: 
			#if element == "4":
				Stein(fenster, 200, 200)
			levelcounter_x = levelcounter_x + 1
			levelcounter_y = int(levelcounter_x / 30)
			#print("x=" + str(levelcounter_x%30) + "y=" + str(levelcounter_y))

pygame.init()


fenster = pygame.display.set_mode((900, 600))
run = True
while run: 
	pygame.time.delay(3)
	for event in pygame.event.get(): #for every event out of the list of all the events happening
		if event.type == pygame.QUIT: #damit wenn man das Fenster zumacht, kein Error kommt
			run = False
	drawlevel(1, fenster)
pygame.quit()
