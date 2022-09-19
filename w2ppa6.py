'''Accept a string as input. If the input string is of odd length, then continue with it. If the input string is of even length, make the string of odd length by following the two steps mentioned below
If the last character is a period (.), then remove it.
If the last character is not a period, then add a period (.) to the end of the string
Call this string of odd length word. Select a substring made up of three consecutive characters from word such that there are an equal number of characters to the left and right of this substring. Print this substring as output. You can assume that all input strings will be in lower case and will have a length of at least four.'''

a = input()

if len(a)%2 == 0:
	if a[-1] == '.':
		a = a[0:len(a)-1]
	else:
		a = a+'.'

p = len(a)//2
word = a[p-1] + a[p] + a[p+1]
print(word)
