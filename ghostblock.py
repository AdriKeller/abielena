import pygame
import block

"""
stellt einen durchlässigen Stein dar (Unterklasse von Block)
"""
class Ghostblock(block.Block):
	"""
	erstellt einen neuen durchlässigen Stein und ruft dabei die init funktion von Block auf
	:param fenster: gibt fenster-Surface weiter um darauf malen zu können
	:param x: x-Position des Blocks (zwischen 0 und 29)
	:param y: y-Position des Blocks (zwischen 0 und 19)
	:param bildsource: path zur Bilddatei des Blocks
	:type fenster: pygame.display
	:type x: int
	:type y: int
	:type bildsource: str
	"""
	def __init__(self, fenster, x, y, bildsource):
		super().__init__(fenster, x, y, bildsource)
	
	def draw(self):
		if True:
			self.fenster.blit(self.bild, (self.x * 30, self.y * 30))
	
"""
stellt einen durchlässigen Stein dar, der duch Button gesteuert wird (Unterklasse von Ghostblock)
"""	
class Buttonghostblock(Ghostblock):
	
	"""
	erstellt einen neuen durchlässigen Stein und ruft dabei die init Funktion von Ghostbecken auf
	:param fenster: gibt fenster-Surface weiter um darauf malen zu können
	:param x: x-Position des Blocks (zwischen 0 und 29)
	:param y: y-Position des Blocks (zwischen 0 und 19)
	:param bildsource: path zur Bilddatei des Blocks
	:param ghostbild: path zur durchsichtigen Bilddatei des Blocks
	:type fenster: pygame.display
	:type x: int
	:type y: int
	:type bildsource: str
	:type ghostbild: str
	"""
	def __init__(self, fenster, x, y, bildsource, ghostbild):
		super().__init__(fenster, x, y, bildsource)
		self.ghostbild = ghostbild
		
		
"""
stellt einen gelben durchlässigen Stein dar, der durch Button gesteuert wird (Unterklasse von Buttonghostblock)
"""	
class Gelberghostblock(Buttonghostblock):
	
	"""
	erstellt einen gelben durchlässigen Stein und ruft dabei die init Funktion von Buttonghostblock auf
	:param fenster: gibt fenster-Surface weiter um darauf malen zu können
	:param x: x-Position des Blocks (zwischen 0 und 29)
	:param y: y-Position des Blocks (zwischen 0 und 19)
	:type fenster: pygame.display
	:type x: int
	:type y: int
	"""
	def __init__(self, fenster, x, y):
		super().__init__(fenster, x, y, "Bilder/gelberblock.png", "Bilder/gelberblock_ghost.png")
		
		
"""
stellt einen lilanen durchlässigen Stein dar, der durch Button gesteuert wird (Unterklasse von Buttonghostblock)
"""	
class Lilaghostblock(Buttonghostblock):
	
	"""
	erstellt einen lilanen durchlässigen Stein und ruft dabei die init Funktion von Buttonghostblock auf
	:param fenster: gibt fenster-Surface weiter um darauf malen zu können
	:param x: x-Position des Blocks (zwischen 0 und 29)
	:param y: y-Position des Blocks (zwischen 0 und 19)
	:type fenster: pygame.display
	:type x: int
	:type y: int
	"""
	def __init__(self, fenster, x, y):
		super().__init__(fenster, x, y, "Bilder/lilablock.png", "Bilder/lilablock_ghost.png")

"""
stellt einen roten durchlässigen Stein dar, der durch Button gesteuert wird (Unterklasse von Buttonghostblock)
"""	
class Roterghostblock(Buttonghostblock):
	
	"""
	erstellt einen roten durchlässigen Stein und ruft dabei die init Funktion von Buttonghostblock auf
	:param fenster: gibt fenster-Surface weiter um darauf malen zu können
	:param x: x-Position des Blocks (zwischen 0 und 29)
	:param y: y-Position des Blocks (zwischen 0 und 19)
	:type fenster: pygame.display
	:type x: int
	:type y: int
	"""
	def __init__(self, fenster, x, y):
		super().__init__(fenster, x, y, "Bilder/roterblock.png", "Bilder/roterblock_ghost.png")


"""
stellt einen durchlässigen Stein dar, der von Player abhängig ist (Unterklasse von Ghostblock)
"""	
class Playerghostblock(Ghostblock):
	
	"""
	erstellt einen neuen durchlässigen Stein pro Player und ruft dabei die init Funktion von Ghostbecken auf
	:param fenster: gibt fenster-Surface weiter um darauf malen zu können
	:param x: x-Position des Blocks (zwischen 0 und 29)
	:param y: y-Position des Blocks (zwischen 0 und 19)
	:param bildsource: path zur Bilddatei des Blocks
	:type fenster: pygame.display
	:type x: int
	:type y: int
	:type bildsource: str
	"""
	def __init__(self, fenster, x, y, bildsource):
		super().__init__(fenster, x, y, bildsource)
		

"""
stellt einen rosanen für P1 durchlässigen Stein dar (Unterklasse von Playerghostblock)
"""	
class P1ghostblock(Playerghostblock):
	
	"""
	erstellt einen rosanen durchlässigen Stein und ruft dabei die init Funktion von Playerghostbecken auf
	:param fenster: gibt fenster-Surface weiter um darauf malen zu können
	:param x: x-Position des Blocks (zwischen 0 und 29)
	:param y: y-Position des Blocks (zwischen 0 und 19)
	:type fenster: pygame.display
	:type x: int
	:type y: int
	"""
	def __init__(self, fenster, x, y):
		super().__init__(fenster, x, y, "Bilder/rosablock.png")
		
		
"""
stellt einen schwarzen für P2 durchlässigen Stein dar (Unterklasse von Playerghostblock)
"""	
class P2ghostblock(Playerghostblock):
	
	"""
	erstellt einen schwarzen durchlässigen Stein und ruft dabei die init Funktion von Playerghostbecken auf
	:param fenster: gibt fenster-Surface weiter um darauf malen zu können
	:param x: x-Position des Blocks (zwischen 0 und 29)
	:param y: y-Position des Blocks (zwischen 0 und 19)
	:type fenster: pygame.display
	:type x: int
	:type y: int
	"""
	def __init__(self, fenster, x, y):
		super().__init__(fenster, x, y, "Bilder/schwarzerblock.png")
