def sum():
    a=int(input("enter the number"))
    i=0
    sum=0
    while i<a:
        num=int(input("enter the number"))
        sum=sum+num
        average=sum//a
        i=i+1
    print("sum:-",sum)
    print("average:-",average)
sum()