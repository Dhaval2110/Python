#method 1
#base class
class abc:
	def __init__(self):
		print("In a base class")

#derived class
class xyz(abc):
	def __init__(self):
		super().__init__()                 #super function is used to call base class in derived 
		print("In a child class")

#Validating if derived class is from base or not
print(issubclass(xyz,abc))                        # True if inherited , False if not

#calling function where c is a consructor
c=xyz()

# method 2
class Dog:
	def __init__(self,name):
		self.name=name

	def descriptor(self):
		return "{} is german shefford".format(self.name)
	
class Gernman(Dog):
	def run(self,speed):
		return "{} runs {}".format(self.name,speed)

c=Gernman("Rocky")
print(c.descriptor())
print(c.run("Slowly"))
