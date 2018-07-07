# -*- coding: utf-8 -*-
#l=[]
import shutil
import sys

f=open('C:\Users\DHAVAL\Desktop\Github.txt','r')

#fd=open('C:\Users\DHAVAL\Documents\dhavalm.txt','r')
fd=open('C:\Users\DHAVAL\Documents\dhavam.txt','a')
#shutil.copyfileobj(fd,sys.stdout)
for line in f:
	fd.write(line)
#fr=open('C:\Users\DHAVAL\Documents\dhavalm.txt','r')
#print fr.read()

import os
#sys.stderr.write=open('C:\Users\DHAVAL\Desktop\Test.txt','w')
import sys

######### To print stderr into a file ##########
f = open("C:\Users\DHAVAL\Desktop\Test.txt", "w")
original_stderr = sys.stderr
sys.stderr = f

os.remove('C:\Users\DHAVAL\Desktop\HAHA.txt')
shutil.rmtree('C:\Users\DHAVAL\Desktop\Dir')
#os.chdir('‪C:\Users\DHAVAL\Desktop')
#sys.stderr.write=open('C:\Users\DHAVAL\Desktop\Test.txt','a')

######## To print stdout into a file ##############
sys.stdout=open('C:\Users\DHAVAL\Desktop\Test.txt','a')
print 'test'

sys.stderr = original_stderr
f.close()