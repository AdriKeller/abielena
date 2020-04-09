import pygame
import block

def drawlevel(levelnumber, fenster):
	blockbild = pygame.image.load("block.png")

	level = open("Level/Level"+ str(levelnumber) + ".txt")
	levelcounter_y = 0
	for line in level:
		levelcounter_x = 0
		for element in line:
			if element == "1":
				fenster.blit(blockbild, (30*levelcounter_x, 30*levelcounter_y))
			levelcounter_x += 1
		levelcounter_y += 1