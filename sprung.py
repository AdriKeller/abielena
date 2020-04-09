import pygame

def jump(player, keypressed):
	if not player.springstate: #gleiches wie = False
			if keypressed:
				player.springstate = True
	else:
		if player.springzahl >= -5: #solange es 5 nicht erreicht
			if player.springzahl > 0:
				neg = 1
			else:
				neg = -1
			player.y = player.y - ((player.springzahl**2)*neg) #bewegung
			player.springzahl = player.springzahl - 2 #counter springzahl
		else: #variablen resetten wenn der sprung fertig ist
			player.springstate = False
			player.springzahl = 5