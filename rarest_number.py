#find most rarest number from a list

a = [1,7,2,1,7,1,3,4,5,6,6,6,7,2,1,9,2]
c, least = len(a), 0
for x in a:
    if a.count(x) <= c :
        c = a.count(x)
        least = x
print("The lest number is {}".format(least)) # 9
