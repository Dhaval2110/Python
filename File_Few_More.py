import sys
import os
import time

c=0
with open(r'C:\Users\DHAVAL\Desktop\abc.txt','r') as f:
	s=f.read()
	print(s)
	for i in s:
		if i.isupper():
			c+=1

print(c,"count")