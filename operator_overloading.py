class addition:
	def __init__(self,a):
		self.a=a
	def __add__(self,o):
		return self.a+o.a

c1=addition(1)
c2=addition(2)
print(c1+c2)
print("Dhaval"+" "+"Mehta")
