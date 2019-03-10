# How to use filter map and lambda in single program

# def even(n):
# 	if n%7==0:
# 		return n
# 	else:
# 		pass

l=range(0,100)
p=list(map(lambda x:x%7==0,l))
print(p)
q=list(filter(lambda x:x%7==0,l))
print(q)


'''
Output : 
[True, False, False, False, False, False, False, True, False, False, False, False, False, False, True, False, False, False, False, False, False, True, False, False, False, False, False, False, True, False, False, False, False, False, False, True, False, False, False, False, False, False, True, False, False, False, False, False, False, True, False, False, False, False, False, False, True, False, False, False, False, False, False, True, False, False, False, False, False, False, True, False, False, False, False, False, False, True, False, False, False, False, False, False, True, False, False, False, False, False, False, True, False, False, False, False, False, False, True, False]
[0, 7, 14, 21, 28, 35, 42, 49, 56, 63, 70, 77, 84, 91, 98]
'''
