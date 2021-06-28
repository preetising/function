def fun(list):
    i=0
    a=[]
    b=[]
    co=0
    while i<len(list):
        if list[i] not in a:
            a.append(list[i])
            b.append(list[i])
        i=i+1
        co=co+1
    print(list,co)
    print("new list=2",b)
fun(list=["Delhi", "Delhi", "Mumbai", "Mumbai", "Delhi", "Chennai", 'Chennai'])

