list=[]
N=int(raw_input())
for i in range (N):
	M=str(raw_input())
	list.append(M)
uppercase=[x.upper() for x in list]
print uppercase
