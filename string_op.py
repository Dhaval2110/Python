# how to replace word in a string called " www.abc.com" where abc to be replaced with every word in l=["mno","pqr","tuv"].
# s="www.abc.com"
# s=s.split('.')
# print(s)
# l=["mno","pqr","tuv"]
# for i in range(0,3):
# 	s[1]=l[i]
# 	print(".".join(s))

# how to remove last element of a list
# l=[1,2,3,4,5,6,7]
# del l[-1]
# print(l)

# How to initialize class with two variables
# class ABC:
# 	def __init__(value,a,b):
# 		value.a=a
# 		value.b=b
# 	def print(value):
# 		print(value.a)
# 		print(value.b)

# c=ABC(10,20)
# c.print()

# how to find capital letters in a file
# l=[]  --> incomplete
# c=0
# fd=open(r"C:\Users\c_dhavme\Desktop\dha\log.txt","r")
# l=fd.readlines()
# print(l)
# for i in l:
# 	if i.upper():
# 		c=c+1
# 	else:
# 		pass
# print(c)

# What is map function? how can i use?
def f(i):
	if i%2==0 and i%5==0:
		return True
	else:
		return False

i=[1,2,3,4,5,6,7,8,9,10]

F=list(map(f,i))
J=list(filter(f,i))
print(J,"J")
print(F,"F")

