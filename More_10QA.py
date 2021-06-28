big_list = [[1,2,3], [5,8,9], [4,3,77,521,31,311]]
counter1 = 0
while counter1 < len(big_list):
    small_list_length = len(big_list[counter1])
    counter2 = 0
    while counter2 < small_list_length:
        print (big_list[counter1][counter2])
        counter2 = counter2 + 1
    counter1 = counter1 + 1
    print ('-----') 