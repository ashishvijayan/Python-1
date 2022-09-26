n = int(input())
if n == 2:
	print('PRIME')
if n > 2:
	flag = False
	for i in range(2, int(n/2)+1):
		if n%i ==0:
			flag = True
			break
if flag:
	print('NOTPRIME')
if not flag:
	print('PRIME')


