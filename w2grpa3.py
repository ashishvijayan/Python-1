'''
Accept a string as input and print the vowels present in the string in alphabetical order. If the string doesn't contain any vowels, then print the string none as output. Each vowel that appears in the input string — irrespective of its case — should appear just once in lower case in the output.
'''

word = input()
word = word.lower()
lst = list(word)
#print(lst)
lst = sorted(lst)
#print(lst)
uniq = []

for i in range(len(lst)):
	if lst[i] not in uniq:
		uniq.append(lst[i])
	
#print(uniq)	

wow = ['a','e','i','o','u']

w = ''

A = True
for j in wow:
	if j in uniq:
		A = False
		w = w + j
		
	if not (A):
		A = False
		
if A:
	print('none')	
else:
	print(w)
		
	


