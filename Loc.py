class Loc:
	def __init__(self,x,y):
		self.x=x
		self.y=y

	def up(self):
		self.y=self.y-10
	
	def down(self):
		self.y=self.y+10

	def left(self):
		self.x=self.x-10

	def right(self):

		self.x=self.x+10	

	def x(self):
		return self.x
	def y(self):
		return self.y		


	def __eq__(self, other):

		return self.x == other.x and self.y == other.y
