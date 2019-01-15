# File examples to read for 

# Global Import
import sys
import os
import time

#Local Import 


# Global variables
c=0

# How to count no of uppercase in file

# with open(r'C:\Users\DHAVAL\Desktop\abc.txt','r') as f:
# 	s=f.read()
# 	print(s)
# 	for i in s:
# 		if i.isupper():
# 			c+=1

# print(c,"count")

#################################################################################

# How to replace word in file

with open(r'C:\Users\DHAVAL\Desktop\abc.txt','r') as fd:
	#content=f.readlines()
	#print(content)
	l=fd.readlines()
	#print(l)
	with open(r'C:\Users\DHAVAL\Desktop\abc.txt','w') as f:
		for i in l:
			#print(i)
			if 'webbrowser' in i:
				#print('true')
				m=i.replace('webbrowser','WOAAA')
				f.write("%s"% m)
			else:
				f.write('%s'%i)
	# for line in content:
	# 	#print(line)
	# 	#print(type(line))
	# 	if "webbroser" in line:
	# 		print("True")
	# 		line=line.replace("webbroser","LOL")

# with open(r'C:\Users\DHAVAL\Desktop\abc.txt','w') as f1:
# 	f1.write('%s' %line)



