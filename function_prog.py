# What is map ,filter and reduce aka function programming?

#Using Traditional Function :)
def abc(i):
	if i%2==0 and i%10==0:
		return i

l=[i for i in range(0,200)]
print(list(map(abc,l)))
print(list(filter(abc,l)))

## print((reduce(abc,l))) ## not sure

#Using Lambda Function :)

l=[i for i in range(0,500)]
x=lambda x:x%2==0 and x%7==0
print(list(map(x,l)))
print(list(filter(x,l)))
