#slope of line formed by collinear points
x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
x3 = float(input())

if x1 == x2:
	print('Vertical Line')
else:

	m = (y1-y2)/(x1-x2)
	y3 = y1 + (x3-x1)*m
	print(y3)
	if m == 0:
		print('Horizontal Line')
	elif m > 0:
		print('Positive Slope')
	elif m < 0:
		print('Negative Slope')

 
