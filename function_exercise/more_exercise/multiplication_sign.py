def greet(*names):
	i=0
	print('Hello ', end='')
	while len(names) > i:
		print(names[i], end=', ')
		i+=1


greet('Steve', 'Bill', 'Yash')
greet('Steve', 'Bill', 'Yash', 'Kapil', 'John', 'Amir')