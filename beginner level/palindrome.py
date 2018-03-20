N=int(raw_input())
Z=N
R=0
while(N>0):
    D=N%10
    R=R*10+D
    N=N//10
if(Z==R):
    print("yes")
else:
    print("no")

    
    
    ANOTHER PROGRAM
   n=raw_input()
N=n[::-1]
if(n==N):
	print("Yes")
else:
	print("No")
