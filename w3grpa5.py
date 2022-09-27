'''Accept a phone number as input. A valid phone number should satisfy the following constraints.

(1) The number should start with one of these digits: 6, 7, 8, 9

(2) The number should be exactly 10 digits long.

(3) No digit should appear more than 7 times in the number.

(4) No digit should appear more than 5 times in a row in the number.

If the fourth condition is not very clear, then consider this example: the number 9888888765 is invalid because the digit 8 appears more than 5 times in a row.

Print the string 'valid' if the phone number is valid. If not, print the string 'invalid'.
'''
num = input()
#print(num[0])

if (num[0] == '6' or num[0] == '7' or num[0] == '8' or num[0] == '9'):
	#print('cool')
	if len(num) == 10:
		#print('kewl')
		flag = False
		
		for i in num:
			count = 0
			for j in num:
				if i == j:
					count +=1
			if count > 7:
				#print('invalid')
				flag = True
				break
		if not flag:
			#print('kaka')
			A = False
		
				
			for k in range(len(num)):
				rep = 0
				B = True
				for l in range(len(num)):
					if num[k] == num[l]:
						rep +=1
					if num[k] != num[l]:
						B == False
						
				if (rep > 5) and B:
					print('invalid')
					A = True
					break
			if not A:
				print('valid')
	else:
		print('invalid')
else:
	print('invalid')
			
		
				
		




