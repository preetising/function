def Harshad():
	sum=0
	c=n
	r=0
	while c>0:
	   r=c%10
	   sum=sum+r
	   c=c//10
	   if n%sum==0:
	   	print('Harshad number')
	   else:
	   	print('not hardhad number')
n=int(input("enter the any number"))
Harshad()


