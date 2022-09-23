def reverse():
	num = abs(int(input('enter the number: ')))
	rev = 0
	while num > 0:
		r = num % 10
		rev = rev * 10 + r
		num = num // 10
	return rev
y = reverse()
print(y)
