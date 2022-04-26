s = """
    this is test paragraph,
    i am tryingh to find the repeated words in this paragraph,
    my goal is to check if same words present in any of the strings,
    this is last line"""
    
    
s= s.split()
d = {}

for i in range(0,len(s)):
    if s[i] not in d:
        d[s[i]]= 0                                  # initialize counter
    d[s[i]] +=1                                     # increment the counter
        
for k,v in d.items():
    print("{} is {} times".format(k,v))
