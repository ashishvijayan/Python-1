def primenum():
	n = int(input('enter the number: '))
	if (n == 1 or n == 2):
		print('none')
	
	if (n > 2):
		print(2, end = ' ') #ends by a space
	
	for i in range(3, n):
		flag = False
		for j in range (2,i):
			if (i % j == 0):
				flag = False
				break
			else:
				flag = True
		if flag:
			print(i, end = ' ')
primenum()
