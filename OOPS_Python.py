# Ref http://net-informations.com/python/iq/init.htm


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

##################################################################

#Q. What is getattr()?

class Person:
    age = 23
    name = "Adam"

person = Person()
print('The age is:', getattr(person, "age"))
print('The age is:', person.age)
#print("Error : ",getattr(person,"Value")) ------> No attributes called value
####################################################################

# Q. What is dir in python?

class Person:
  def __dir__(self):
    return ['age', 'name', 'salary']
    

teacher = Person()
print(dir(teacher))


##########################################################################

