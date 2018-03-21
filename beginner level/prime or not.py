N=int(raw_input())
Z=0
for i in (2,N/2,1):
	if(N%i==0):
		Z=1
	else:
		break
if(Z==0):
	print("yes")
else:
	print("no")
