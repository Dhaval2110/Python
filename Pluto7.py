## Questions 
1 . c=1 
    def one():
        #global c
        #print(c)
        for i in (1,2,3):
            print("hi")
            c=+1 
           #print(c)
    one()
    print(c)
# Ans : Hi and 1

2. c=1 
def one():
    #global c
    print(c)
    for i in (1,2,3):
        print("hi")
        c=+1 
        #print(c)
one()
print(c)
# Ans: Error....
3. c=1 
def one():
    global c
    #print(c)
    for i in (1,2,3):
        #print("hi")
        c=+1 
        #print(c)
one()
print(c)
#Ans :[Original] 1

#NEW
4. 
print('klljllklklkkl'.replace('kl','22',0)) # -----> klljllklklkkl , no affect as third argument is 0
print('klljllklklkkl'.replace('kl','22'))   # -----> 22ljll2222k22 , swap source and dec

5. 
def lis(k):
    print(k)
    k[0]=1 
    
two=[0]
lis(two)
print(two)
# Ans : [1] , we can pass list as an argument of a function

