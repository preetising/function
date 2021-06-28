def fun():
    i=0
    a=[]
    b=list1+list2
    while i<len(list1):
        if list1[i] not in a:
            a.append(list1[i]) 
        i=i+1
        a.sort()
    print(a)
list1=[1, 5, 10, 12, 16, 20]
list2=[1, 2, 10, 13, 16]
fun()
