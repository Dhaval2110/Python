# Different sorting methods

#1. Sort a list by first alphabet

# l=['dhaval','mehta','united','FCBarca','spain']
# s=[]
# count=65
# while len(s)<len(l):
# 	for i in range(0,len(l)):
# 		if ord(l[i][:1])==count:
# 			s.append(l[i])
# 			count+=1
# 	count+=1

# print(s)
# print(sorted(l))

# How to reverse a string 
s=list("Dhaval")
s.reverse()
print(''.join(s))
##or
s=s[::-1]
print(''.join(s))
