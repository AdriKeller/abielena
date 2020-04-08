if not p1.springstate: #gleiches wie = False
		if allkeys[pygame.K_UP] :
			p1.springstate = True
	else:
		if springzahl_f >= -5: #solange es 5 nicht erreicht
			if springzahl_f > 0:
				neg = 1
			else:
				neg = -1
			feuer_y = feuer_y - ((springzahl_f**2)*neg) #bewegung
			springzahl_f = springzahl_f - 2 #counter springzahl
		else: #variablen resetten wenn der sprung fertig ist
			p1.springstate = False
			springzahl_f = 5
	if not springstate_w: #gleiches wie = False
		if allkeys[pygame.K_w] :
			springstate_w = True
	else: 
		if springzahl_w >= -5:
			if springzahl_w > 0:
				neg = 1
			else:
				neg = -1
			wasser_y = wasser_y - ((springzahl_w**2)*neg) #neg weil es erst hoch dann runter muss
			springzahl_w = springzahl_w - 2
		else: #variablen resetten wenn der sprung fertig ist
			springstate_w = False
			springzahl_w = 5
			
