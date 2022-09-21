a_name = input('your name: ')
a_dob = input('your dob in DD-MM-YYYY: ')
b_name = input('your name: ')
b_dob = input('your dob in DD-MM-YYYY: ')

if int(b_dob[6:]) < int(a_dob[6:]):
	print(a_name)
elif int(a_dob[6:]) < int(b_dob[6:]):
	print(b_name)
	
elif int(b_dob[6:]) == int(a_dob[6:]):

	if int(a_dob[3:5]) > int(b_dob[3:5]):
		print(a_name)
	elif  int(b_dob[3:5]) > int(a_dob[3:5]):
		print(b_name)
	elif  int(a_dob[3:5]) == int(b_dob[3:5]):
	
		if int(a_dob[0:2]) > int(b_dob[0:2]):
			print(a_name)
		elif int(b_dob[0:2]) > int(a_dob[0:2]):
			print(b_name)
		elif int(a_dob[0:2]) == int(b_dob[0:2]):
		
			if a_name < b_name:
				print(a_name)
			else:
				print(b_name)
			
		
		
		
	
	
	
	

