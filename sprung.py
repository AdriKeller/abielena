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
			
