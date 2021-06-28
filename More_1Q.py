def fun():
    i=0
    while i<num:
        if i%21==0:
            return ("nav")
        elif i%7==0:
            return "gurukul"
        elif i%3==0:
            return "navgurukul"
        i=i+1
num=int(input("enter the number"))
print(fun())