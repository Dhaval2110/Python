
##### https://www.sanfoundry.com/python-problems-solutions/ ########
"""
# avg value
l=[1,11,25,48,65,32,89]
e=len(l)
s=0
for i in l:
	s=s+i
avg=s/e
print(avg)

#swapping of variable
a=10
b=20
a=a+b         #c logic
b=a-b
a=a-b
print(a)
print(b)
a,b=b,a #one liner
print(a)
print(b)

#compute 
n=int(input("Enter a number n: "))
temp=n
t1=temp+temp
t2=temp+temp+temp
comp=n+int(t1)+int(t2)
print("The value is:",comp)

# reverse a num
n=123
s=0
while (n):
	s=s*10+(n%10)
	n=n//10
print(s)

# Positive or negative 
n=610
if n&1<<31 is 0:
	print("True")
else:
	print("False")

# divisible in a range
l=[]
for i in range(1,200):
	if i%5==0 and i%10!=0:
		l.append(i)

print(l)

# print reminder and quotient

a=int(input("enter the num1"))
b=int(input("enter the num 2"))
r=a%b
q=a//b
print(q,"quotient")
print(r,"reminder")

# Combinations -- Good one 
a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
c=int(input("Enter third number:"))
d=[]
d.append(a)
d.append(b)
d.append(c)
for i in range(0,3):
    for j in range(0,3):
        for k in range(0,3):
            if(i!=j&j!=k&k!=i):
                print(d[i],d[j],d[k])


# odd it out

for i in range(1,25):
	if i%2!=0:
		print(i,end=' ')


# sum of digits

n=134
s=0
while n>0:
	s=s+(n%10)
	n=n//10

print(s)


# Smallest divisor
n=7
l=[]
for i in range(2,n+1):
	if n%i==0:
		l.append(i)

l.sort()
print(l[0])

# no of digits in a num
n=123456
c=0
while n>0:
	c=c+1
	n=n//10
print(c)


# palindrom

n=12321
num=n
s=0
while n:
	s=s*10+(n%10)
	n=n//10
print(s)
if s==num:
	print(True)
else:
	print(False)


# Print the series 1+2+.....+n
n=int(input("Enter a number: "))
a=[]
for i in range(1,n+1):
    print(i,sep=" ",end=" ")
    if(i<n):
        print("+",sep=" ",end=" ")
    a.append(i)
print("=",sum(a))
 
print()

# identity matrix

n=int(input("Enter a number: "))
for i in range(0,n):
    for j in range(0,n):
        if(i==j):
            print("1",sep=" ",end=" ")
        else:
            print("0",sep=" ",end=" ")
    print()

# Pattern of **
n=int(input("Enter number of rows: "))
for i in range (n,0,-1):
    print((n-i) * ' ' + i * '*')

# list examples

even=[]
odd=[]
l=[1,3,4,5,7,8,11,34,56,8,5,7]
for i in range(0,len(l)):
	for j in range(0,len(l)):
		if l[i]<l[j]:
			t=l[i]
			l[i]=l[j]
			l[j]=t

print(l[-1],"largest")
print(l[-2],"second")

print(l)
for i in l:
	if (i%2==0):
		even.append(i)
	else:
		odd.append(i)

print(even,"-> Even Elements list")
print(odd,"-> Odd Elements list")

# take 2 list and merge into single , sort it
l1=[]
l2=[]
for i in range(0,5):
	n=input("Enter the elements")
	l1.append(n)
print(l1,"List 1")
for i in range(0,5):
	n=input("Enter the elements")
	l2.append(n)
print(l2,"List 2")

l=len(l2)

new=l1+l2 # concate string
print(new) # apply soring algo

l=new
for i in range(0,len(l)):
	for j in range(0,len(l)):
		if l[i]<l[j]:
			t=l[i]
			l[i]=l[j]
			l[j]=t
print(new,"mine")
new.sort()
print(new,"in built")


#sort a list according to length of an elemet

l=["Dhaval","Mehta","Manchester","SW","IOT"]
t=''
for i in range(0,len(l)):
	for j in range(0,len(l)):
		if len(l[i])>len(l[j]):
			t=l[i]
			l[i]=l[j]
			l[j]=t
print(l)


# Find a union of two lists
l1=[2,3,6,7,9,11]
l2=[9,5,11,2,8,6,7]
l3=[]
for i in range(0,len(l1)):
	for j in range(0,len(l2)):
		if l1[i]==l2[j]:
			l3.append(l1[i])

print(l3)

# Python Program to Create a List of Tuples with the First Element as the Number and Second Element as the Square of the Number
l=[(x,x**2) for x in range(1,5)]
print(l)


# Just list comprehensions exercise

l=[i for i in range(21) if i%2==0 and i%5!=0]
print(l)

a=[]
for i in range(21):
	if i%2==0 and i%5!=0:
	   a.append(i)
print(a)


# Random no generate between 1 to 20

l=[]
import random
l.append(random.randint(1,20))
print(l)

# Swap first and last element of a list

l=[1,2,3,4,5]
t=l[-1]
l[-1]=l[0]
l[0]=t
print(l)

# remove duplicatr in the list

s=[]
l=[1,2,3,1,1,3,4,5,6]

for i in l:
    if i not in s:
        s.append(i)

print(s)
print(set(l))

# alphabatic sort

l=['dhaval','mehta','united','FCBarca','spain']
s=[]
count=65
while len(s)<len(l):
	for i in range(0,len(l)):
		if ord(l[i][:1])==count:
			s.append(l[i])
			count+=1
	count+=1

print(s)
print(sorted(l))

# Python Program to Read a List of Words and Return the Length of the Longest One

# bubble sort

l=['dhaval','mehta','Manchester','California','gujarat','vadodara']
t=" "
for i in range(0,len(l)-1):
    for j in range(0,len(l)-i-1):
        if len(l[j])>len(l[j+1]):
            t=l[j]
            l[j]=l[j+1]
            l[j+1]=t

print(l)
print(len(l[-1]))


# remove ith occurance of given in alist where word can repeat        ----- Incomplete

l=['apple','apple','ball','cat','cat']

a=[]
for i in l:
     if 'cat'!=str(l[i]):
       a.append(l[i])

print(a)

####################### STRRRIIIIINNNGGGGGGSSSS ################

# Replace all 'a' with $

s="dhaval"
s=s.replace('a','$')
print(s)

# Remove the nth Index Character from a Non-Empty String

s="dhaval"
n=4

for i in range(0,len(s)):
    if i==n:
        s=s.replace(s[i],'')

print(s)


# Find the no of vowels in a sring


s="my name is manchester united"
l=['a','e','i','o','u']
c=0
for i in range(0,len(s)):
	for j in range(0,len(l)):
		if s[i]==l[j] :
		   c=c+1
print(c)

# Form a New String where the First Character and the Last Character have been Exchanged

s="dhaval"
s=s[-1:]+s[1:-1]+s[:1]              # IMP Logic
print(s)

"""
#Take in a String and Replace Every Blank Space with Hyphen

s="my name is manchester united"
for i in s:
	if i == " ":
		s=s.replace(i,'-')

print(s)
