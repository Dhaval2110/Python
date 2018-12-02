
def fact(n):
	if n==0:
		return 1
	else:
		return n*fact(n-1)

n=5
s=fact(n)
print(s)


# fIbonacci
a, b = 0, 1
while b < 100:
    print(b)
    a, b = b, a + b 
	
	
	
	#OR


def fib(n):
	if n==0 or n==1:
		return 1
	else:
		return fib(n-1)+fib(n-2)

n=10
for i in range(0,n):
	s=fib(i)
	print(s)
