import sys, pygame, copy


class Worm:
	def __init__(self,st):
		self.st=st
		self.direction = 'up'

		self.downpic = pygame.image.load('snakedown.png')
		self.downpic = pygame.transform.scale(self.downpic, (20,20))

		self.uppic = pygame.image.load('snakeup.png')
		self.uppic = pygame.transform.scale(self.uppic, (20,20))

		self.leftpic = pygame.image.load('snakeleft.png')
		self.leftpic = pygame.transform.scale(self.leftpic, (20,20))

		self.rightpic = pygame.image.load('snakeright.png')
		self.rightpic = pygame.transform.scale(self.rightpic, (20,20))

	def length(self):
		return len(self.st)	

	def setdir(self,newdir):
		self.direction = newdir	

	def add(self,last): 
		
		self.st.append(last)

	def update(self):
		if self.direction == 'up':
			self.up()

		elif self.direction == 'down':
			self.down()
		elif self.direction == 'left':
			self.left()
		elif self.direction == 'right':
			self.right()		


	def extend(self, last):
		self.st.extend(last)	
		

	def get(self,x):
		return self.st[x]

	def left(self):
		self.direction = 'left'
		temp=copy.deepcopy(self.st[0])
		self.st[0].left()
		for x in range(1,len(self.st)):
			temp2=copy.deepcopy(self.st[x])
			self.st[x]=copy.deepcopy(temp)
			temp=copy.deepcopy(temp2)

	def right(self):
		self.direction = 'right'
		temp=copy.deepcopy(self.st[0])
		self.st[0].right()
		for x in range(1,len(self.st)):
			temp2=copy.deepcopy(self.st[x])
			self.st[x]=copy.deepcopy(temp)
			temp=copy.deepcopy(temp2)		

	def up(self):
		self.direction = 'up'
		temp=copy.deepcopy(self.st[0])
		self.st[0].up()
		for x in range(1,len(self.st)):
			temp2=copy.deepcopy(self.st[x])
			self.st[x]=copy.deepcopy(temp)
			temp=copy.deepcopy(temp2)		

	def down(self):
		self.direction = 'down'
		temp=copy.deepcopy(self.st[0])
		self.st[0].down()
		for x in range(1,len(self.st)):
			temp2=copy.deepcopy(self.st[x])
			self.st[x]=copy.deepcopy(temp)
			temp=copy.deepcopy(temp2)		

	def getlocation(self):
		return self.st[0]

	def checkloc(self,loc):
		for x in range(0,len(self.st)):
			if (self.st[x] == loc):
				return True
		return False

	def display(self,screen):
		if self.direction == 'down':
			screen.blit(self.downpic,(2*self.st[0].x, 2*self.st[0].y))

		if self.direction == 'up':
			screen.blit(self.uppic,(2*self.st[0].x, 2*self.st[0].y))

		if self.direction == 'left':
			screen.blit(self.leftpic,(2*self.st[0].x, 2*self.st[0].y))	

		if self.direction == 'right':
			screen.blit(self.rightpic,(2*self.st[0].x, 2*self.st[0].y))	
		for x in range(1,len(self.st)):
			pygame.draw.circle(screen, (0,255,0), (2*self.st[x].x+10, 2*self.st[x].y+10), 2*5, 0)
				