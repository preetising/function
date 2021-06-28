def budget(amount,student):
    c=len(student)
    total=c*amount
    if amount<=50000:
        print(total,"under the buget")
    else:
        print(total,"over baget")
amount=int(input("enter the amount"))
budget(amount,["Preeti""Rani","ujala","Deepti","pooja"])