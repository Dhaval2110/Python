# Example

# Iterator

class ABC():
	def __init__(self,start,end):
		self.start=start
		self.end=end
	def __iter__(self):
		return self
	def __next__(self):
		if self.start>self.end:
			raise StopIteration
		else:
			self.start +=1
			return self.start

c=ABC(0,10)
for i in c:
	print(i, end=' ')

print('\n')

# For loop is working as an iterator

for i in range(1,12):
	print(i,end = ' ')
  

# Generator 


def my_gen():
	print("Inside generator")
	yield 'a'
	yield 'b'
	yield 'c'

for i in my_gen():
	print(i)
 
