# how to replace word in a string called " www.abc.com" where abc to be replaced with every word in l=["mno","pqr","tuv"].
s="www.abc.com"
s=s.split('.')
print(s)
l=["mno","pqr","tuv"]
for i in range(0,3):
	s[1]=l[i]
	print(".".join(s))
