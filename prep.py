#1. List a=[ 1,2,3 none, none] list b=[4,5,3] Output=[1,4,2,5,3,3] ?
#
# list1=[1,2,3]
# list2=[4,5,6]
# result=[]
# result = [0]*(len(list1)+len(list2))                                            # Creating empty list with element of total of the two lists
# print(result)
# result[0::2] =list1                                                             # List 1 first member to be at 0 and step as 2
# result[1::2]=list2                                                              # List 2 first element to be at 1 and step as 2
# print(result)

#2.Given two variables and asked two exchange the values between them without
# using third varible

#method 1
# a=10
# b=20
# print("Before swap")
# print(a,"a")
# print(b,"b")
# a+=b
# b=a-b
# a=a-b
# print("After swap")
# print(a,"a")
# print(b,"b")

#method 2
# a=10
# b=20
# print("After swap")
# print(a,"a")
# print(b,"b")
# a,b=b,a
# print("After swap")
# print(a,"a")
# print(b,"b")


#fctorial
# def fact(n):
# 	if n==0 | n==1:
# 		return 1
# 	else:
# 		return n*fact(n-1)

# n=3
# s=fact(n)
# print(s)

# #fib
# def fib(n):
# 	if n==0 or n==1:
# 		return 1
# 	else:
# 		return fib(n-1)+fib(n-2)

# n=10
# for i in range(n):
# 	s=fib(i)
# 	print(s)

#remove duplicate

# l=[1,2,1,1,2,2,3,4,4,2]
# s=[]
# for i in l:
# 	if i not in s:
# 		s.append(i)

# print(s)


# largest from list
l=[2,12,22,34,5,11,54,90]

for i in range(0,len(l)):
	for j in range(0,len(l)-1):
		if l[i]>l[j]:
			t=l[i]
			l[i]=l[j]
			l[j]=t

print(l)