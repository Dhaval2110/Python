# Ref http://net-informations.com/python/iq/init.htm
####NVIDIA#####

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
##ARM##

# Q. How to remove duplicates from list without using set() function?
s=[]
l=[1,1,2,3,3,2,1,2,3,4,5,5,5,5,7]
for i in l:
    if i not in s:
        s.append(i)

print(set(l))
print (s)

##################################################################################

# Q. Let a =[1,2,3,4,5] then what will be the output of a[2],a[2:],a[10],a[10:]?
a=[1,2,3,4,5]
print(a[2])                #-----> O/P = 3
print(a[2:])               #-----> O/P =[3,4,5]
#print(a[10])              #-----> O/P = List out of index
print(a[10:])              #-----> O/P = [] , an empty list

#####################################################################################
# Q. I have a directory named Dhaval inside i have subfolders names test1,test2...and each subfolder
# is consist of files having names as test1.c,test2.c etc. How to change subfolder and files names
# from test to Dhaval without changing digit conventions?
## eg : Dhaval\Test1\test1.c,test2.c --->Dhaval\Dhaval1\Dhaval1.c,Dhaval2.c....
import os
s=''
for root,dirs,files in os.walk(r'C:\Users\DHAVAL\Desktop\Old resumes'):
    for f in files:
        if f.startswith('Dhaval'):
            s=f.replace('Dhaval','Resume')
            os.rename(os.path.join(root,f),os.path.join(root,s))

###############################################################################################
# Q. How will you print a file removing first five and last 10 lines form a file?
l=[]
with open('C:/Users/Dhaval/Desktop/record.txt','r')as f:
    l=f.readlines()
    l=l[2:-7]
    with open('C:/Users/Dhaval/Desktop/record.txt','w') as fd:
        for item in l:
            fd.write("%s" % item)