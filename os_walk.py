# How to find a file from a folder and replace a line with new line 
import os
l=[]
for root,paths,files in os.walk(r'C:\Users\DHAVAL\Desktop\Old_resumes'):
	if 'ooo.txt' in files:
		r=os.path.join(root,'ooo.txt')
		with open(r,'r') as fd:
			l=fd.readlines()
			with open(r,'w') as f:
				for i in l:
					if 'Dhaval Mehta' in i:
						m=i.replace('Dhaval Mehta','WOAAA')
						f.write("%s"% m)
					else:
						f.write('%s'%i)
