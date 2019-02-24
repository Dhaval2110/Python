# How to iterate over Dictionary
d={'Dhaval':10,'mehta':11,'united':12}
for i,j in d.items():
	print("key is {}".format(i))
	print("value is {}".format(j))
  
# How to add or delete element in dictionary

d={'India':1,'USA':2,'Germany':3}
print(d)
d['Australia']=4                              # Add key value pair
print(d)
del d['India']
print(d)
# d.pop('India')                                # To remove key value pair
# print(d)
