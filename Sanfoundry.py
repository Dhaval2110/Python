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
# Form a New String where the First Character and the Last Character have been
Exchanged
s="dhaval"
s=s[-1:]+s[1:-1]+s[:1]              # IMP Logic
print(s)
#Take in a String and Replace Every Blank Space with Hyphen
s="my name is manchester united"
for i in s:
	if i == " ":
		s=s.replace(i,'-')
print(s)
# Calculate the Length of a String Without Using a Library Function
s="my name is dhaval"
c=0
for i in s:
    if i!='\0':
        c=c+1
print(c,"count")
#Characters of Odd Index Values in a String
#s="dhaval mehta"
s="hello"
f=""
for i in range(0,len(s)):
    if i%2==0:
        f=f+s[i]
print(f)
# Calculate the Number of Words and the Number of Characters Present in a String
s="I am manchester united fan"
word=1
char=0
for i in s:
    if i==" ":
        word=word+1
    if i!="\0":
        char=char+1
print("No of words",word)
print("No of char",char)
# Take in Two Strings and Display the Larger String without Using Built-in
#  Functions
import sys
a=sys.argv[1]
b=sys.argv[2]
c1=0
c2=0
for i in a:
    if i!="\0":
        c1=c1+1
for i in b:
    if i!="\0":
        c2=c2+1
if c1>c2:
    print("%s"% a,"String is greater")
elif c2>c1:
    print("%s"% b,"String is greater")
else:
    print("Both are same")
# Count Number of Lowercase Characters in a String without in built function
s="My name is dhaval"
c=0
for i in range(len(s)):
    if (ord(s[i])>=97 and ord(s[i])<=122):
        c=c+1
print(c)
# Check if a String is a Palindrome or Not
s="malayalam"
c=s[::-1]
if s==c:
    print("String is palindrom")
else:
    print("String is not palindrom")
#Calculate the Number of Upper Case Letters and Lower Case Letters in a String
s="My Name Is Dhaval"
l=0
u=0
space=0
for i in range(len(s)):
    if ord(s[i])>=97 and ord(s[i])<=122:
        l=l+1
    elif ord(s[i])>=62 and ord(s[i])<=96:
        u=u+1
    else:
        space=space+1
print(l)
print(u)
print(space)
#Count the Occurrences of Each Word in a Given String Sentence
a=[]
s="my name is dhaval, dhaval is a decent person"
sub="is"
a=s.split(" ")
c=0
for i in range(len(a)):
    if sub==a[i]:
        c=c+1
print(c)
# Form a New String Made of the First 2 and Last 2 characters From a Given
# String
c=0
s="Manchester United"
# for i in s:
#     c=c+1
#l=s[0:2]+s[c-2:c]
l=s[0:2]+s[-2:]
print(l)


# Check if a Substring is Present in a Given String

s="Mo salah is still the king of premier league"
sub="is"
if s.find(sub)==-1:
    print("False")
else:
    print("True")


 # Add a Key-Value Pair to the Dictionary

d={'name':'dhaval','value':'10','team':'manchester'}
d.update({'player':'Cristiano'})
print(d)

# Concatenate Two Dictionaries Into One

d={'name':'dhaval','Dream':'NASA'}
d1={'New':'ISRO'}
d.update(d1)
print(d)

# P.S. Try with giving same keys :)

# Check if a Given Key Exists in a Dictionary or Not

d={'name':'dhaval','value':'10','team':'manchester'}
key='team'
if key in d.keys():
	print("Present", d[key])
else:
	print("Not present")


#  Dictionary that Contains Numbers (between 1 and n) in the Form (x,x*x)
d={x:x*x for x in range(0,4)}
print(d)


# Sum All the Items in a Dictionary

d={'A':100,'B':540,'C':239}
s=0
for i in d.values():
	s=s+i
print(s)

# Multiply All the Items in a Dictionary
d={'A':100,'B':540,'C':239}
s=1
for i in d.values():
	s=s*i
print(s)

# Remove the Given Key from a Dictionary
d={'A':100,'B':540,'C':239}
#n=d.pop('C')
del d['C']
print(d)


# Form a Dictionary from an Object of a Class

class A:
	def __init__(self,name,data):
		self.name=name
		self.data=data

a=A("Dhaval","Mehta")
print(a.__dict__)


# Map Two Lists into a Dictionary

l1=[1,3,5,7,9]
l2=[2,4,6,8,10]
d=dict(zip(l1,l2))
print(d)


# Count the Frequency of Words Appearing in a String Using a Dictionary --> Good One

test_string="My name is dhaval, today is monday, My head is paining"
l=[]
l=test_string.split()
wordfreq=[l.count(p) for p in l]
print(dict(zip(l,wordfreq)))

# Count the Number of Vowels Present in a String using Sets

s="my name is dhaval"
v=set("aeiou")
print(v)
c=0
for i in s:
	if i in v:
		c=c+1

print(c)

# Common Letters in Two Input Strings

d="dhaval"
m="mehta"
a=(set(d)&set(m))
print(a)

# Displays which Letters are in the First String but not in the Second

a="dhaval"
b="manchester"
s=set(a)-set(b)
print(s)


#Displays which Letters are Present in Both the Strings
a="dhaval"
b="manchester"
s=set(a)|set(b)
print(s)

#  Displays which Letters are in the Two Strings but not in Both
a="dhaval"
b="manchester"
s=set(a)^set(b)
print(s)

# Whether a Given Number is Even or Odd Recursively

n=int(input("Enter the number"))
def eo(n):
	if(n<2):
		return(n%2==0)
	return(eo(n-2))
if(eo(n)==True):
	 print("Number is even!")
else:
      print("Number is odd!")


#Determine How Many Times a Given Letter Occurs in a String Recursively

s=input("Enter the string")
c=input("Enter the char")

def char_pres(s,c):
	count=0
	for i in s:
		if i==c:
			count=count+1
	return count
t=char_pres(s,c)
print(t)

# Fibonacci series

a=0
b=1

n=int(input("Enter the number in Fibonacci"))

def fib(n):
	if n<=1:
		return n
	else:
		return((fib(n-1))+fib(n-2))

for i in range(n):
	print(fib(i))

"""
