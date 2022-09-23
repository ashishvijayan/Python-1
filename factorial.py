def factorial(n):
	if n == 0 or n==1:
		return 1
	else:
		return (n*factorial(n-1))

num = int(input('enter the number: '))
print('number: ', num, 'factorial: ', factorial(num))


'''
n = int(input('enter the number: '))


if n ==0 or n == 1:
	print(1)
else:
	fact =  1
	while n > 1:
		fact = fact*n
		n-=1
	print('factorial: ', fact)	


	





