"""
This is bubble sort in python
"""
s=[1,11,2,4,3,9,5,7]
for i in range(0,len(s)):
	for j in range(0,len(s)):
		if s[i] > s[j]:
			t=s[i]
			s[i]=s[j]
			s[j]=t 

print(s)
