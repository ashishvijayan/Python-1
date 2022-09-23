def noofdigits():
	n = abs(int(input('enter the number: ')))
	digit = 1
	while n > 9:
		n = n//10
		print(n)
		digit +=1
	return digit
y = noofdigits()
print(y)
