''' Accept a positive integer nn as input and print the sum of the first nn terms of the series given below:
1+ (1 + 2) + (1 + 2 + 3) + (1 + 2 + 3 + 4) + .... '''

n = int(input())
sum = 0
for i in range(1,n+1):
	inc = 1
	for j in range(i):
		sum = sum + inc
		inc = inc + 1
print(sum)
		
		
		
	
