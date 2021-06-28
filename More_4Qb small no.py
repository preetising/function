def fun(a,b,c):
    if a<b and a<c:
        print("a is smaller")
    elif b<a and b<c:
        print("b is smaller")
    elif c<a and c<b:
        print("c is smaller")
    else:
        print("we are equal")
a=int(input("enter the no"))
b=int(input("enter the no "))
c=int(input("enter the no"))
fun(a,b,c)

