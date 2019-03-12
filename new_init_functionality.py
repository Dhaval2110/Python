'''
Reference : https://spyhce.com/blog/understanding-new-and-init
'''
'''
class A(object):  # -> don't forget the object specified as base

    def __new__(cls):
        print "A.__new__ called"
        return super(A, cls).__new__(cls)

    def __init__(self):
        print "A.__init__ called"

A()
'''
#best example in which first __new__ is called before __init__

class ABC:
	def __new__(cls,*args,**kwargs):
		print("In a __new__")
		print(cls,"Class")
		print(*args,"Args")
		#print(**kwargs,"kwargs")
		return super(ABC,cls).__new__(cls)
	def __init__(self,a,b):
		print("In a __init__")
		self.a=a
		self.b=b
	def printdata(self):
	 	print(self.a,"a")
	 	print(self.b,"b")

c=ABC(10,20)
c.printdata()
