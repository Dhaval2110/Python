#Logics to reverse the string

name="Dhaval"

1. Using in build function
print("".join(reversed(name)))

2. Using slicing
print(name[::-1])

3. Using loop
l=""
for i in name:
	l=i+l
print(l)
