list1=[1,2,3]
list2=[4,5,6]
result=[]
result = [0]*(len(list1)+len(list2))                                            # Creating empty list with element of total of the two lists
print(result)
result[0::2] =list1                                                             # List 1 first member to be at 0 and step as 2
result[1::2]=list2                                                              # List 2 first element to be at 1 and step as 2
print(result)
