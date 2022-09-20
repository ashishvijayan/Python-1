'''The sum of the employee-ids of every pair of adjacent employees at the table must be an even number. They sit in a circle. They are so lazy that they won't move around to satisfy the above condition. If the current seating plan doesn't satisfy the condition, the meeting will be canceled. You are given the employee-id of all five employees. Your task is to decide if the meeting happened or not.The input will be five lined, each line containing an integer. The i th
line will have the employee-id of Ei. The output will be a single line containing one of these two strings: YES or NO.'''

e1 = int(input())
e2 = int(input())
e3 = int(input())
e4 = int(input())
e5 = int(input())

l = [e1, e2, e3, e4, e5]

flag = True
for i in range(len(l)):
	if i == (len(l)-1):
		if ((l[(len(l)-1)] + l[0]) % 2) == 0:
			flag = True
		else:
			flag = False
	if i < (len(l)-1):
			
		if ((l[i] + l[i+1]) % 2) == 0:
			flag = True
		else:
			flag = False
			break
if flag:
	print('YES')
if not flag:
	print('NO')		
	
	

