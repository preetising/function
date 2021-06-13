def min(numbers):
	i=0
	min=numbers[0]
	while i<len(numbers):
		if numbers[i]<min:
			min=numbers[i]
		i+=1
	print(min)
numbers=[3,5,7,34,2,89,2,5]
min(numbers)
