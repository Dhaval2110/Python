#Q: Define class has 2 arguments name and age and print it 
class ABC:
	def __init__(self,name,age):
		self.name=name
		self.age=age
	def data(self):
		print self.name
		print self.age

c=ABC('Dhaval',10)
c.data()
#print c.name
#rint c.age

##############################################

#Q. How can we print base and child in inheritance ----->SUPER() in python


class Base(object):
    def __init__(self):
        print "Base created"

class ChildA(Base):
    def __init__(self):
        #Base.__init__(self)
        super(ChildA,self).__init__()
        #super().__init__() ----> python 3
        print "ChildA"
        #super(ChildA,self).__init__()

# class ChildB(Base):
#     def __init__(self):
#     	print "ChildB"
#         #super(ChildB, self).__init__()

ChildA() 
#ChildB()