'''
Question: How Do I Copy An Object In Python?

Answer :

In general, try copy.copy() or copy.deepcopy() for the general case. Not all objects can be copied, but most can.
Some objects can be copied more easily. Dictionaries have a copy() method:
newdict = olddict.copy()
Sequences can be copied by slicing:
new_l = l[:]
'''
#EX:
# 1. Shallow Copy  ---> Address wise copy 
import copy
b=[]
c=[]
l=[1,2,3,4,5]
b=l
l[2]=-1
print(l)
print(b)
# 2. Deep copy ---> Member wise copy
c=copy.deepcopy(l)
l[2]=-11
print(l)
print(c)
