import pygame
import block
def drawlevel(levelnumber):
	level = open("Level/Level"+ str(levelnumber) + ".txt")
	levelcounter = 0
	for line in level:
		for element in line:
			if element == "1":
				return fenster.blit(block.block1, (30+levelcounter, 30+levelcounter))
			levelcounter = levelcounter + 1
drawlevel(1)
