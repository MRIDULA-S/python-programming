N=int(raw_input())
a=0
b=1
for i in range(0,N):
    c=a+b
    a=b
    print a
    b=c
