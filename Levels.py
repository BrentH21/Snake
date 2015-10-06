import pygame
from Loc import Loc
from random import randint
class Levels:
	def __init__(self, num):
	
		self.num = num;
		self.wood = pygame.image.load('wood.png')
		self.wood = pygame.transform.scale(self.wood, (250,40))

		self.vertwood = pygame.image.load('vertwood.png')
		self.vertwood = pygame.transform.scale(self.vertwood, (40,250))

		self.dirt = pygame.image.load('dirt.jpg')
		self.dirt = pygame.transform.scale(self.dirt, (878,778)).convert()

		self.lvl3 = pygame.image.load('lvl3.png')
		self.lvl3 = pygame.transform.scale(self.lvl3, (300,600))

		self.lvl3up = pygame.image.load('lvl3up.png')
		self.lvl3up = pygame.transform.scale(self.lvl3up, (300,600))

	

	def display(self, screen):
		if (self.num ==1):

			screen.blit(self.dirt,(61,141))
			screen.blit(self.wood,(60,520))
			screen.blit(self.wood,(680,520))

			screen.blit(self.vertwood,(480,150))
			screen.blit(self.vertwood,(480,660))

		if (self.num == 2):
			screen.blit(self.lvl3,(100,280))	
			screen.blit(self.lvl3,(220,180))

			screen.blit(self.lvl3up, (600,180))
			screen.blit(self.lvl3up, (480,280))



	def number(self):
	    return self.num;

	def checkloc(self,loc):
		x=loc.x*2
		y=loc.y*2

		if loc.x >460 or loc.x<30:
			return True
		if loc.y <70 or loc.y >450:
			return True 			



		if (self.num ==1):
			if (x>60 and x<310 and y>510 and y<560):
				return True

			if (x>660 and y>510 and y<560):
				return True	

			if (x>470 and x<520 and y<390):
				return True	

			if (x>470 and x<520 and y>650):
				return True	

		if self.num == 2:
			if (x>90 and x<150 and y>270 and y<880):
				return True

			if (x>90 and x<400 and y <880 and y>810):
				return True	


			if (x>210 and x<270 and y>170 and y<780):
				return True
			if (x>210 and x<520 and y <780 and y>710):
				return True

			if (x>590 and x<900 and y>170 and y<240):
				return True

			if (x>820 and x<900 and y>170 and y<780):
				return True

			if (x>470 and x<780 and y>270 and y<340):
				return True
			
			if (x>700 and x<780 and y>270 and y<880):
				return True	






					



		return False		





		
