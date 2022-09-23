def palindrome():
	num = abs(int(input('enter the number: ')))
	n = num
	rev = 0
	while n > 0:
		r = n % 10
		rev = rev * 10 + r
		n = n // 10
	if rev == num:
		print('yes, ', num, ' is a palindrome')
	else:
		print('not palindrome')
	
palindrome()
