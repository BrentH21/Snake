import pygame
from Loc import Loc
from random import randint

class Food:
	def __init__(self):
		self.location= Loc(10*randint(3,44),10*randint(7,40))

		self.apple = pygame.image.load('apple.png')
		self.apple = pygame.transform.scale(self.apple, (20,20))

	def reset(self):
		self.location = Loc(10*randint(3,44),10*randint(7,40))

	def getlocation(self):
		return self.location

	def display(self,screen):

		screen.blit(self.apple,(2*self.location.x, 2*self.location.y))#drawing food