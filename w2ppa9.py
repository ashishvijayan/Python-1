total = int(input('no of coins: '))
a = int(input('coins given to a: '))
b = int(input('coins given to b: '))
c = int(input('coins given to c: '))

if a!=0 and b!=0 and c!= 0:
	if a!=b and b!=c and a!= c:
		if (a + b + c) == total:
			print('FAIR')
			
		else:
			print('UNFAIR')
	else:
		print('UNFAIR')
else:
	print('UNFAIR')
	
