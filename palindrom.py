s="madam"
l=0
r=len(s)-1
flag=0
while r>=l:
	if not s[r]==s[l]:
		flag=1
	l=l+1
	r=r-1

if flag==1:
	print("not")
else:
	print("Yes")
'''
for number:
n=121
num=n
s=0
while n:
	s=s*10+(n%10)
	n=n//10

if s is num:
	print("True")
else:
	print("no")
'''
