import sys, pygame, copy
from random import randint
from Worm import Worm
from Loc import Loc
from Food import Food
from Levels import Levels
pygame.init()

global ssize
ssize  = 800,800

size = width, height = 1000, 1000



screen=pygame.Surface((size),32)
window = pygame.display.set_mode((ssize), pygame.RESIZABLE)


###########################################LOADING IMAGES################################################################

pausepic = pygame.image.load('pause.jpg')
pausepic = pygame.transform.scale(pausepic, (1000,1000))

menupic = pygame.image.load('menu.jpg')
menupic = pygame.transform.scale(menupic, (1000,1000))



scoref = pygame.font.Font('WHITRABT.ttf', 32) #font for the length
pausetxt = scoref.render("p - to pause ", True, (0,255,0) ) 

bigname = pygame.font.Font('WHITRABT.ttf', 85)
snakename = bigname.render('Snake', True, (0,255,0))

lvlpic = pygame.image.load('level.jpg')
lvlpic = pygame.transform.scale(lvlpic, (1000,1000))

#############################################################################################################################

def game(levels):
		
		global level 
		level = levels

		global foodlet
		global wormlet 

		foodlet = Food()
		prt1=Loc(250,250)
		wormlet = Worm([prt1])
		
		game = True
		
		while game == True:

			last = copy.deepcopy(wormlet.get(wormlet.length()-1))
	
			events = pygame.event.get()
			for event in events:
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_LEFT:
						wormlet.setdir('left')
					
					elif event.key == pygame.K_RIGHT:
						wormlet.setdir('right')

					elif event.key == pygame.K_UP:
						wormlet.setdir('up')

					elif event.key == pygame.K_DOWN:
						wormlet.setdir('down')

					elif event.key == pygame.K_q:
						game = False

					elif event.key == pygame.K_p:
						a = pause()
						if a == 'menu':
							game = False

			
			wormlet.update() #advances worm in its direction
						
			first=wormlet.get(0)
			
			if foodlet.getlocation() == wormlet.getlocation():
				wormlet.add(last)
				foodlet.reset()
			while (level.checkloc(foodlet.getlocation()) == True or wormlet.checkloc(foodlet.getlocation()) == True):
				foodlet.reset()
							
			display()

			if (level.checkloc(first) == True):
				game = False
	
			for x in range (1, wormlet.length()):
				if first == wormlet.get(x):
					game = False
			
			window.blit(pygame.transform.smoothscale(screen,(ssize)),(0,0))
			pygame.display.flip()
			pygame.display.update()	
			if level.num == 2:
				pygame.time.wait(45)
			elif level.num == 1:
				pygame.time.wait(65)
			else:
				
				pygame.time.wait(80)

def display():

	screen.fill((0,0,0))
	level.display(screen)  #display overlay for specific level
	score = scoref.render("Score: "+str(wormlet.length()), True, (0,255,0) ) 

	screen.blit(score,(800,20) )  #position to display the score
	screen.blit(pausetxt, (100,20))
	screen.blit(snakename,(400,20))

	pygame.draw.rect(screen, (0,128,255), (60,140, 880,780), 3)

	foodlet.display(screen)
	
	
	wormlet.display(screen)	

	

def menu():
	screen.fill((0,0,0))
	menu = True
	screen.blit(menupic,(0,0))
	window.blit(pygame.transform.scale(screen,(ssize)),(0,0))
	pygame.display.flip()

	while menu == True:
		pygame.time.wait(10)
		events = pygame.event.get()
		for event in events:
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_a:
					screen.blit(lvlpic,(0,0))
					window.blit(pygame.transform.scale(screen,(ssize)),(0,0))
					pygame.display.flip()
					while 1 == 1:
						pygame.time.wait(10)
						events = pygame.event.get()
						for event in events:
							if event.type == pygame.KEYDOWN:
								if event.key == pygame.K_a:
									return '1playerEasy'
								if event.key == pygame.K_b:
									return '1playerMed'
								if event.key == pygame.K_c:
									return '1playerHard'		



				if event.key == pygame.K_q:
					pygame.quit()

def main(): #main menu
	main = True
	

	while main == True:
		first = menu()

		if first == '1playerEasy':
			game(Levels(0))

		if first == '1playerMed':
			game(Levels(1))
			
		if first == '1playerHard':
			game(Levels(2))
		



def pause():
	pause = True
	screen.fill((0,0,0))
	screen.blit(pausepic,(0,0) )
	window.blit(pygame.transform.scale(screen,(ssize)),(0,0))
	pygame.display.flip()
				
			
	while pause == True:
		pygame.time.wait(10)
		events = pygame.event.get()
		for event in events:
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_a:
					screen.fill((0,0,0))
					display()
					pause == False
					return 'a' 

				if event.key == pygame.K_b:
					return 'menu'


				if event.key == pygame.K_q:
					pygame.quit()
					pause = False
					return 'a'





if __name__ == "__main__":
	main()







