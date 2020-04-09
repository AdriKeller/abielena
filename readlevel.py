import pygame
import block
x = 0
y = 0
def drawlevel(levelnumber, fenster):
	level = open("Level/Level"+ str(levelnumber) + ".txt")
	levelcounter_x = 0
	levelcounter_y = 0
	for line in level:
		for element in line: 
			if element == "1":
				fenster.blit(block.block1, (30 +levelcounter_x, 30+levelcounter_y))
			levelcounter_x = levelcounter_x + 1
			levelcounter_y = int(levelcounter_x / 30)
			#print("x=" + str(levelcounter_x%30) + "y=" + str(levelcounter_y))

pygame.init()


fenster = pygame.display.set_mode((900, 600))

drawlevel(1, fenster)
