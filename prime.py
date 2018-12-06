
def prime(n):
	flag=1
	for i in range(2,n):
		if n%i==0:
			flag=0
			#sys.exit()
	if flag==1:
		print("Prime")
	else:
		print("Not")

prime(41)
