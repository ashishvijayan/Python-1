'''A sequence of five words is called magical if the i^{th}i 
th word is a substring of the (i + 1)^{th}(i+1) 
th word for every ii in the range 1 \leq i < 51≤i<5. Accept a sequence of five words as input, one word on each line. Print magical if the sequence is magical and non-magical otherwise.Note that str_1 is a substring of str_2 if and only if str_1 is present as a sequence of consecutive characters in str_2.'''

str_1 = input()
str_2 = input()
str_3 = input()
str_4 = input()
str_5 = input()
lst = [str_1, str_2, str_3, str_4, str_5]
flag = True
for i in range(len(lst)):
	if i < (len(lst)-1):
		if lst[i] in lst[i+1]:
			flag = True
		else:
			flag = False
			break
		
if flag:
	print('magical')
if not flag:
	print('non-magical')		

