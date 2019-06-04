def rev(s):
    l = len(s)
    for i in range(l-1, -1, -1):
        yield (s[i])


for char in rev("dhaval"):
    print(char, end="")
