'''
 Suppose class B inherits from class A. Both have the method sayhello()- to each, their own version. B overrides the sayhello() of class A. So, when we create an object of class B, it calls the version that class B has.
'''

class A:
	def sayhello(self):
		print("Hello, I'm A")
class B(A):
	def sayhello(self):
		print("Hello, I'm B")
a=A()
b=B()
a.sayhello()
b.sayhello()
