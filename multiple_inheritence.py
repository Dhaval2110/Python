class ABC:
	def __init__(self,a,b):
		self.a=a
		self.b=b
	# def print(self):
	# 	print(self.a)
	# 	print(self.b)
class MNO:
	def __init__(self):
		print("In MNO Base class")
class DEF(ABC,MNO):                              #multi_level
	def __init__(self,c,d):
		self.c=c
		self.d=d
		super().__init__(10,20)
		MNO.__init__(self)

	def print(self):
		print("Value of a is {}".format(self.a))
		print("Value of b is {}".format(self.b))
		print("Value of c is {}".format(self.c))
		print("Value of d is {}".format(self.d))

c=DEF(30,40)
c.print()

