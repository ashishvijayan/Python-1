
def bishops_route():
'''Accept two positions as input: start and end. Print YES if a bishop at start can move to end in exactly one move. Print NO otherwise. Note that a bishop can only move along diagonals.'''

	start = input('where does your bishop sit: ')
	end = input('where is it going: ')
	
	row_step = abs(int(start[1]) - int(end[1]))
	column_step = abs(ord(start[0]) - ord(end[0]))
	#print('row step:', row_step, 'column step:', column_step)
	
	if row_step == column_step:
		print('YES')
	else:
		print('NO')
		
bishops_route()
	
	
	

