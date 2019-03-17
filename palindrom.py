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
