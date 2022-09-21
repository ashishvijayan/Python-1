'''Accept a string as input. Your task is to determine if the input string is a valid password or not.'''
password = input('enter your password:')
err = ['/', '\\', '=', "'",'"',' ']

if len(password) >= 8 and len(password) <= 32:
	if password[0].isalpha():
		flag = True
		for i in err:
			if i in password:
				flag = False
				break
		if flag:
			print(True)	
		else:
		    print(False)
	else:
		print(False)
		
else:
	print(False)
	

