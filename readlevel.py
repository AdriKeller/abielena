level = open("Level/Level1.txt")
levelcounter = 0
for line in level:
	for element in line:
		print(element)
		levelcounter = levelcounter + 1
