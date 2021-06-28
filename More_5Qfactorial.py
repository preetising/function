def fun(n):
    fac=1
    i=n
    while i>0:
        fac=fac*i
        i=i-1
    return "factorial =",fac
n=int(input("enter the number"))
print(fun(n))