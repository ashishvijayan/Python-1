n = int(input())
for i in range(2,n+1):
	flag = True
	for j in range(2,i):
		
		if i!=j:
			if i%j == 0:
				flag = False
				break
	if flag:
		if n % i == 0:
			print(i)
