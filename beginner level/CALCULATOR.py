print("1.Addition")
print("2.Subtraction")
print("3.Division")
print("4.Multiplication")
print("5.AND")
print("6.OR")
print("7.Modulo")
print("8.Power")
print("9.Floor Division")
print("10.Not Equal")
print("Enter the selection (1 to 10)")
select=int(input())
a=int(input())
b=int(input())
if select==1:
	print(a+b)
elif select==2:
	print(a-b)
elif select==3:
	print(a/b)
elif select==4:
	print(a*b)	
elif select==5:
	print(a&b)	
elif select==6:
	print(a|b)
elif select==7:
	print(a%b)
elif select==8:
	print(a**b)
elif select==9:
	print(a//b)
else :
	print(a!=b)
