#checking pythagorean triplets
a = int(input())
b = int(input())
c = int(input())

k = 0

if a > b:
	k = a
	a = b
	b = k
if c < a:
	k = a
	a = c
	c = k
if c < b:
	k = b
	b = c
	c = k
	
if (a**2 + b**2) == c**2:
	print('YES')
else:
	print('NO')

'''a = int(input())
b = int(input())
c = int(input())

l = [a,b,c]
l.sort()

if ((l[0]**2 + l[1]**2) == l[2]**2):
	print('YES')
else:
	print('NO')
'''
